import csv
from models.user import userbase, updateuser, userID, createuser
from enums import *

data_base = "user.csv"

column_fields = [
    "id",
    "id_type",
    "id_number",
    "name",
    "email",
    "diabetes_type",
]

def auto_id():
    try:
        with open(data_base,"r") as csvfile:
            reader = csv.DictReader(csvfile, column_fields)
            max_id = max(
                int(row["id"]) for row in reader
            )
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1


def write_user_into_csv(register: userID):
    with open(
        data_base, mode="a", newline=""
    ) as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=column_fields,
        )
        writer.writerow(register.model_dump())


def create_animal(user: userbase):
    new_id = auto_id()
    new_user_ID = userID(
        id=new_id,
        **user.model_dump()
    )

    write_user_into_csv(new_user_ID)
    return new_user_ID

def read_all_animals():
    with open(data_base) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=column_fields)
        return [userbase(**row) for row in reader]

def read_one_animal_by_id(user_id: str):
    with open(data_base) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=column_fields)
        for row in reader:
            if row["id"] == user_id:
                return userbase(**row)
        return None



