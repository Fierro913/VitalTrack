from pydantic import BaseModel, EmailStr, Field
from enums.id_type import IdType
from enums.Diabetes_type import DiabetesType


class UserBase(BaseModel):
    id: str
    id_type: IdType
    id_number: str
    name: str
    email: EmailStr
    diabetes_type: DiabetesType
    status: str = "active"


class CreateUser(BaseModel):
    id_type: IdType
    id_number: str = Field(min_length=1)
    name: str = Field(min_length=1)
    email: EmailStr
    diabetes_type: DiabetesType


class UpdateUser(CreateUser):
    pass