import csv
from pathlib import Path
from models.glucose_register import Register, CreateRegister, UpdateRegister

DATA_BASE = Path(__file__).resolve().parent.parent / "glucose_register.csv"
FIELDS = ["id", "user_id", "date", "glucose_mg_dl", "moment", "comida_id", "notes", "status"]


def initialize_csv():
    if not DATA_BASE.exists():
        with DATA_BASE.open("w", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=FIELDS).writeheader()


def get_registers() -> list[Register]:
    initialize_csv()
    with DATA_BASE.open("r", newline="", encoding="utf-8") as file:
        rows = []
        for row in csv.DictReader(file):
            row["comida_id"] = row["comida_id"] or None
            rows.append(row)
        return [Register.model_validate(row) for row in rows]


def get_active_registers() -> list[Register]:
    return [r for r in get_registers() if r.status == "active"]


def get_registers_by_user(user_id: str) -> list[Register]:
    return [r for r in get_active_registers() if r.user_id == user_id]


def create_register(new_register: CreateRegister) -> Register:
    initialize_csv()
    data = new_register.model_dump(mode="json")
    data["id"] = str(len(get_registers()) + 1)
    data["status"] = "active"
    with DATA_BASE.open("a", newline="", encoding="utf-8") as file:
        csv.DictWriter(file, fieldnames=FIELDS).writerow(data)
    return Register.model_validate(data)


def save_registers(registers: list[Register]):
    initialize_csv()
    with DATA_BASE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for r in registers:
            writer.writerow(r.model_dump(mode="json"))


def update_register(register_id: str, data: UpdateRegister) -> Register | None:
    registers = get_registers()
    for i, current in enumerate(registers):
        if current.id == register_id and current.status == "active":
            updated = data.model_dump(mode="json")
            updated["id"] = register_id
            updated["status"] = current.status
            registers[i] = Register.model_validate(updated)
            save_registers(registers)
            return registers[i]
    return None


def delete_register(register_id: str) -> bool:
    registers = get_registers()
    for r in registers:
        if r.id == register_id and r.status == "active":
            r.status = "inactive"
            save_registers(registers)
            return True
    return False