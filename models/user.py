from pydantic import BaseModel, ConfigDict, EmailStr
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
    status: str = "active"


class createuser(BaseModel):
    id_type: IdType
    id_number: str
    name: str
    email: EmailStr
    diabetes_type: DiabetesType


class updateuser(createuser):
    id_type: IdType
    id_number: str
    name: str
    email: EmailStr
    diabetes_type: DiabetesType



