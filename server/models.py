from pydantic import BaseModel
from typing import Optional

class Action(BaseModel):
    action_type: str
    value: Optional[str] = None

