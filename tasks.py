from sqlmodel import select
from app.db import session_scope
from app.models import Task, Approval, AuditEvent
from app.tools.safe_tools import registry

def create_task(command: str):
    with session_scope() as s:
        task = Task(command=command)
        s.add(task); s.commit(); s.refresh(task)
        approval = Approval(task_id=task.id, action="execute_task")
        s.add(approval)
        s.add(AuditEvent(actor="local-admin", event="task.created", detail=f"task_id={task.id}"))
        s.commit()
        return task, approval

def list_tasks():
    with session_scope() as s:
        return s.exec(select(Task).order_by(Task.id.desc())).all()

def decide(approval_id: int, approve: bool, reason: str):
    with session_scope() as s:
        approval = s.get(Approval, approval_id)
        if not approval:
            return None
        approval.status = "approved" if approve else "rejected"
        approval.decided_at = __import__("datetime").datetime.now(__import__("datetime").timezone.utc)
        task = s.get(Task, approval.task_id)
        if task:
            if approve:
                tool = registry.get("prepare_task")
                result = tool.handler(task.command)
                task.status = "prepared"
                task.result = str(result)
            else:
                task.status = "rejected"
        s.add(AuditEvent(actor="local-admin", event="approval.decided",
                         detail=f"approval_id={approval_id};approved={approve};reason={reason}"))
        s.add(approval)
        if task: s.add(task)
        s.commit()
        return approval, task

def audit_events():
    with session_scope() as s:
        return s.exec(select(AuditEvent).order_by(AuditEvent.id.desc()).limit(200)).all()
