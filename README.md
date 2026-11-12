# AI Agent Automation — PC Enterprise Edition

A cross-platform (Windows/Linux/macOS) desktop-oriented agent platform starter.
It includes a FastAPI control plane, authenticated API foundation, role-based access
hooks, approval-gated tools, audit events, a local dashboard, browser automation
adapter, and optional desktop-control adapter.

## What is actually included
- FastAPI API with health, task, approval and audit endpoints
- SQLite development persistence
- API-key authentication for local single-tenant development
- Tool registry with allow-listing and approval requirements
- Browser automation adapter using Playwright (optional install)
- Desktop automation adapter using PyAutoGUI (optional install)
- Task execution worker loop (local in-process development worker)
- Audit event records
- Docker configuration
- Example `.env` with placeholders

## Not production certified
This is a strong engineering starter, not a finished enterprise product. Before real
company deployment add PostgreSQL, Redis/Celery or Temporal, SSO/OIDC, tenant isolation,
secrets vault, centralized logs/metrics/tracing, backups, rate limits, threat modeling,
security review, deployment hardening and load tests. Do not expose the development API
directly to the public internet.

## Quick start (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
Open http://127.0.0.1:8000/docs

## Quick start (Linux/macOS)
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## Browser automation
Install optional browser dependencies:
```bash
pip install -r requirements-browser.txt
playwright install chromium
```
Browser actions must be limited to websites and accounts the operator is authorized to use.
The included browser tool opens a URL and returns page title/text; it does not bypass logins,
CAPTCHAs, paywalls, or platform restrictions.

## Desktop automation
Install `requirements-desktop.txt` separately. PyAutoGUI controls the local machine and can
be dangerous if misused. Keep it disabled until the operator enables it locally and test
with non-destructive actions. A visible emergency stop and action confirmation are required
before enabling write/submit actions.

## API
- `GET /health`
- `POST /api/v1/tasks`
- `GET /api/v1/tasks`
- `POST /api/v1/approvals/{approval_id}/decision`
- `GET /api/v1/audit`

Authentication: set `AGENT_API_KEY` in `.env` and send `X-API-Key`.
