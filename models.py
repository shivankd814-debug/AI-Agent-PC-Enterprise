from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field

def now():
    return datetime.now(timezone.utc)

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    command: str
    status: str = "pending_approval"
    result: str = ""
    created_at: datetime = Field(default_factory=now)

class Approval(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int
    action: str
    status: str = "pending"
    decided_at: Optional[datetime] = None

class AuditEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    actor: str
    event: str
    detail: str
    created_at: datetime = Field(default_factory=now)
