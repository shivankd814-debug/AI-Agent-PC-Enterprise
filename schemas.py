from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    command: str = Field(min_length=2, max_length=4000)

class ApprovalDecision(BaseModel):
    approve: bool
    reason: str = Field(default="", max_length=500)
