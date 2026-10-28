from pydantic import BaseModel, Field


class FoodBase(BaseModel):
    user_id: str
    name: str = Field(min_length=1)
    carbs_g: float = Field(ge=0)


class CreateFood(FoodBase):
    pass


class UpdateFood(FoodBase):
    pass


class Food(FoodBase):
    id: str
    status: str = "active"