from pydantic import BaseModel, Field
from typing import Optional, List


class Observation(BaseModel):
    complaint: str
    category: Optional[str] = None
    priority: Optional[str] = None
    department: Optional[str] = None
    status: str = "pending"
    delay: int = 0
    history: List[str] = Field(default_factory=list)


class Action(BaseModel):
    action_type: str
    value: Optional[str] = None


class Reward(BaseModel):
    score: float
    reason: str