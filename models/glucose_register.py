from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from enums.day_moment import Moment


class RegisterBase(BaseModel):
    user_id: str
    date: datetime
    glucose_mg_dl: float = Field(gt=0, le=1000)
    moment: Moment
    comida_id: Optional[str] = None
    notes: str


class CreateRegister(RegisterBase):
    pass


class UpdateRegister(RegisterBase):
    pass


class Register(RegisterBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    status: str = "active"