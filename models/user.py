from pydantic import BaseModel, ConfigDict, EmailStr
from enums.id_type import IdType
from enums.Diabetes_type import DiabetesType


class userbase(BaseModel):
    id: str
    id_type: IdType
    id_number: str
    name: str
    email: EmailStr
    diabetes_type: DiabetesType


class createuser(BaseModel):
    id_type: IdType
    id_number: str
    name: str
    email: EmailStr
    diabetes_type: DiabetesType


class updateuser(BaseModel):
    id_type: IdType
    id_number: str
    name: str
    email: EmailStr
    diabetes_type: DiabetesType


class user(userbase):
    model_config = ConfigDict(from_attributes=True)

