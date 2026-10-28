import csv
from pathlib import Path
from models.food import Food, CreateFood, UpdateFood

DATA_BASE = Path(__file__).resolve().parent.parent / "food.csv"
FIELDS = ["id", "user_id", "name", "carbs_g", "status"]


def initialize_csv():
    if not DATA_BASE.exists():
        with DATA_BASE.open("w", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=FIELDS).writeheader()


def get_foods() -> list[Food]:
    initialize_csv()
    with DATA_BASE.open("r", newline="", encoding="utf-8") as file:
        return [Food.model_validate(row) for row in csv.DictReader(file)]


def get_active_foods() -> list[Food]:
    return [f for f in get_foods() if f.status == "active"]


def get_foods_by_user(user_id: str) -> list[Food]:
    return [f for f in get_active_foods() if f.user_id == user_id]


def create_food(new_food: CreateFood) -> Food:
    initialize_csv()
    data = new_food.model_dump(mode="json")
    data["id"] = str(len(get_foods()) + 1)
    data["status"] = "active"
    with DATA_BASE.open("a", newline="", encoding="utf-8") as file:
        csv.DictWriter(file, fieldnames=FIELDS).writerow(data)
    return Food.model_validate(data)


def save_foods(foods: list[Food]):
    initialize_csv()
    with DATA_BASE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for f in foods:
            writer.writerow(f.model_dump(mode="json"))


def update_food(food_id: str, data: UpdateFood) -> Food | None:
    foods = get_foods()
    for i, current in enumerate(foods):
        if current.id == food_id and current.status == "active":
            updated = data.model_dump(mode="json")
            updated["id"] = food_id
            updated["status"] = current.status
            foods[i] = Food.model_validate(updated)
            save_foods(foods)
            return foods[i]
    return None


def delete_food(food_id: str) -> bool:
    foods = get_foods()
    for f in foods:
        if f.id == food_id and f.status == "active":
            f.status = "inactive"
            save_foods(foods)
            return True
    return False