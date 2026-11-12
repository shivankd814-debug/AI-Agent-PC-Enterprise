from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from app.db import init_db
from app.security import require_api_key
from app.schemas import TaskCreate, ApprovalDecision
from app.services.tasks import create_task, list_tasks, decide, audit_events
from app.tools.safe_tools import registry
from app.tools.desktop import get_desktop_status

app = FastAPI(title="AI Agent Automation — PC Enterprise", version="1.0.0")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok", "service": "pc-agent-control-plane"}

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return '''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>AI Agent Automation</title><style>
    body{font:16px system-ui;background:#0b1020;color:#e8edff;margin:40px;max-width:900px}
    .card{background:#151d33;padding:22px;border-radius:16px;margin:14px 0}
    input,button{padding:12px;border-radius:8px;border:0}button{background:#7c6cff;color:white}
    </style></head><body><h1>AI Agent Automation</h1><p>PC Enterprise Control Plane</p>
    <div class="card"><h3>API ready</h3><p>Open <a href="/docs">API documentation</a>. Use authenticated endpoints with X-API-Key.</p></div>
    <div class="card"><h3>Safety by design</h3><p>Tasks are queued for approval. Browser and desktop control are disabled by default.</p></div></body></html>'''

@app.get("/api/v1/tools", dependencies=[Depends(require_api_key)])
def tools():
    return {"tools": registry.list(), "desktop": get_desktop_status()}

@app.post("/api/v1/tasks", dependencies=[Depends(require_api_key)])
def submit_task(payload: TaskCreate):
    task, approval = create_task(payload.command)
    return {"task": task, "approval": approval, "message": "Task created; approval required."}

@app.get("/api/v1/tasks", dependencies=[Depends(require_api_key)])
def tasks():
    return list_tasks()

@app.post("/api/v1/approvals/{approval_id}/decision", dependencies=[Depends(require_api_key)])
def approval_decision(approval_id: int, payload: ApprovalDecision):
    result = decide(approval_id, payload.approve, payload.reason)
    if result is None:
        raise HTTPException(404, "Approval not found")
    approval, task = result
    return {"approval": approval, "task": task}

@app.get("/api/v1/audit", dependencies=[Depends(require_api_key)])
def audit():
    return audit_events()
