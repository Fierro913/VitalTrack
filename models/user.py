from pydantic import BaseModel, EmailStr,Field
from typing import Optional
from enums.id_type import IdType
from enums.Diabetes_type import DiabetesType
class userbase(BaseModel):
    id: str
    id_type: IdType
    id_number: str
    name: str
    email: EmailStr
    diabetes_type: DiabetesType

class userID(userbase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class createuser(userbase):
    pass

class updateuser(userbase):
    nombre: str
    email: EmailStr
    diabetes_type: DiabetesType

class user(userbase):
    model_config = ConfigDict(from_attributes=True)
    id: str

