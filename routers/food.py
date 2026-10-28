from fastapi import APIRouter, status, HTTPException
from models.food import food, createfood, updatefood
from data.food import create_food, get_foods, get_foods_by_user, update_food, delete_food
router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=food)
def create_food_endpoint(new_food: createfood):
    return create_food(new_food)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[food])
def show_all_foods():
    foods = get_foods()
    if not foods:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No foods found")
    return foods


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=list[food])
def show_foods_by_user(user_id: str):
    foods = get_foods_by_user(user_id)
    if not foods:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No foods found for this user")
    return foods


@router.patch("/{food_id}", status_code=status.HTTP_200_OK, response_model=food)
def update_food_endpoint(food_id: str, new_food: updatefood):
    updated = update_food(food_id, new_food)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food not found")
    return updated


@router.delete("/{food_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_food_endpoint(food_id: str):
    if not delete_food(food_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food not found")