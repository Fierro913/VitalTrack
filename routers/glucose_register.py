from fastapi import APIRouter, status, HTTPException
from models.glucose_register import register, createRegister, UpdateRegister
from data.glucose_register import (
    create_register, get_registers, get_register, update_register, delete_register
)

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=register)
def create_register_endpoint(new_register: createRegister):
    return create_register(new_register)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[register])
def show_all_registers():
    registers = get_registers()
    if not registers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No registers found")
    return registers


@router.get("/{register_id}", status_code=status.HTTP_200_OK, response_model=register)
def show_one_register(register_id: str):
    found = get_register(register_id)
    if found is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Register not found")
    return found


@router.patch("/{register_id}", status_code=status.HTTP_200_OK, response_model=register)
def update_register_endpoint(register_id: str, new_register: UpdateRegister):
    updated = update_register(register_id, new_register)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Register not found")
    return updated


@router.delete("/{register_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_register_endpoint(register_id: str):
    if not delete_register(register_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Register not found")