import csv
from pathlib import Path
from models.user import UserBase, CreateUser, UpdateUser

DATA_BASE = Path(__file__).resolve().parent.parent / "user.csv"
FIELDS = ["id", "id_type", "id_number", "name", "email", "diabetes_type", "status"]

def initialize_csv():
    if not DATA_BASE.exists():
        with DATA_BASE.open("w", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=FIELDS).writeheader()

def get_users() -> list[UserBase]:
    initialize_csv()
    with DATA_BASE.open("r", newline="", encoding="utf-8") as file:
        return [UserBase.model_validate(row) for row in csv.DictReader(file)]


def get_active_users() -> list[UserBase]:
    return [u for u in get_users() if u.status == "active"]


def get_user(user_id: str) -> UserBase | None:
    return next((u for u in get_active_users() if u.id == user_id), None)


def create_user(new_user: CreateUser) -> UserBase:
    initialize_csv()
    data = new_user.model_dump(mode="json")
    data["id"] = str(len(get_users()) + 1)
    data["status"] = "active"
    with DATA_BASE.open("a", newline="", encoding="utf-8") as file:
        csv.DictWriter(file, fieldnames=FIELDS).writerow(data)
    return UserBase.model_validate(data)


def save_users(users: list[UserBase]):
    initialize_csv()
    with DATA_BASE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for user in users:
            writer.writerow(user.model_dump(mode="json"))


def update_user(user_id: str, data: UpdateUser) -> UserBase | None:
    users = get_users()
    for i, current in enumerate(users):
        if current.id == user_id and current.status == "active":
            updated = data.model_dump(mode="json")
            updated["id"] = user_id
            updated["status"] = current.status
            users[i] = UserBase.model_validate(updated)
            save_users(users)
            return users[i]
    return None


def delete_user(user_id: str) -> bool:
    users = get_users()
    for user in users:
        if user.id == user_id and user.status == "active":
            user.status = "inactive"
            save_users(users)
            return True
    return False