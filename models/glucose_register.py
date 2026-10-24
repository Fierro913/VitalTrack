from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from enums.day_moment import Moment

class RegisterBase(BaseModel):
    user_id: str
    date: datetime
    glucose_mg_dl: float
    moment: Moment
    comida_id:str
    notes:str

class createRegister(RegisterBase):
    pass

class UpdateRegister(RegisterBase):
    user_id: str
    date: datetime
    glucose_mg_dl: float
    moment: Moment
    comida_id:str
    notes:str

class register(RegisterBase):
    model_config = ConfigDict(from_attributes=True)
    id:str