from pydantic import BaseModel, ConfigDict, Field

class FoodBase(BaseModel):
    user_id:str
    name:str
    carbs_g:float

class createfood(FoodBase):
    pass

class updatefood(FoodBase):
    user_id:str
    name:str
    carbs_g:float

class food(FoodBase):
    model_config = ConfigDict(from_attributes=True)
    id: str