from fastapi import APIRouter, status, HTTPException
from models.glucose_register import Register, CreateRegister, UpdateRegister
from data.glucose_register import (
    create_register, get_active_registers, get_registers_by_user, update_register, delete_register
)
from data.user import get_user
from data.food import get_active_foods

router = APIRouter()


def check_references(data):
    if get_user(data.user_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if data.comida_id is not None:
        if not any(f.id == data.comida_id for f in get_active_foods()):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food not found")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Register)
def create_register_endpoint(new_register: CreateRegister):
    check_references(new_register)
    return create_register(new_register)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[Register])
def show_all_registers():
    registers = get_active_registers()
    if not registers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No registers found")
    return registers


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=list[Register])
def show_registers_by_user(user_id: str):
    registers = get_registers_by_user(user_id)
    if not registers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No registers found for this user")
    return registers


@router.patch("/{register_id}", status_code=status.HTTP_200_OK, response_model=Register)
def update_register_endpoint(register_id: str, new_register: UpdateRegister):
    check_references(new_register)
    updated = update_register(register_id, new_register)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Register not found")
    return updated


@router.delete("/{register_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_register_endpoint(register_id: str):
    if not delete_register(register_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Register not found")