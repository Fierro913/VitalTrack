from pydantic import BaseModel, EmailStr,Field
from typing import Optional
from enums.Diabetes_type import DiabetesType
class userbase(BaseModel):
    name: str
    email: EmailStr
    diabetes_type: DiabetesType

class userID(userbase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

