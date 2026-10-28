import csv
from pathlib import Path
from models.user import userbase, createuser, updateuser

DATA_BASE = Path(__file__).resolve().parent.parent / "user.csv"
FIELDS = ["id", "id_type", "id_number", "name", "email", "diabetes_type", "status"]

def initialize_csv():
    if not DATA_BASE.exists():
        with DATA_BASE.open("w", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=FIELDS).writeheader()

def get_users() -> list[userbase]:
    initialize_csv()
    with DATA_BASE.open("r", newline="", encoding="utf-8") as file:
        return [userbase.model_validate(row) for row in csv.DictReader(file)]


def get_user(user_id: str) -> userbase | None:
    return next((u for u in get_users() if u.id == user_id), None)


def create_user(new_user: createuser) -> userbase:
    initialize_csv()
    data = new_user.model_dump(mode="json")
    data["id"] = str(len(get_users()) + 1)
    data["status"] = "active"
    with DATA_BASE.open("a", newline="", encoding="utf-8") as file:
        csv.DictWriter(file, fieldnames=FIELDS).writerow(data)
    return userbase.model_validate(data)


def save_users(users: list[userbase]):
    initialize_csv()
    with DATA_BASE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for user in users:
            writer.writerow(user.model_dump(mode="json"))


def update_user(user_id: str, data: updateuser) -> userbase | None:
    users = get_users()
    for i, current in enumerate(users):
        if current.id == user_id:
            updated = data.model_dump(mode="json")
            updated["id"] = user_id
            updated["status"] = current.status
            users[i] = userbase.model_validate(updated)
            save_users(users)
            return users[i]
    return None


def delete_user(user_id: str) -> bool:
    users = get_users()
    filtered = [user for user in users if user.id != user_id]
    if len(filtered) == len(users):
        return False
    save_users(filtered)
    return True
