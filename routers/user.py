from fastapi import APIRouter, status, HTTPException
from models.user import UserBase, CreateUser, UpdateUser
from data.user import create_user, get_active_users, get_user, update_user, delete_user

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserBase)
def create_user_endpoint(new_user: CreateUser):
    '''
    Create a new user in the platform
    '''
    return create_user(new_user)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserBase])
def show_all_users():
    '''
    Show all users in the platform
    '''
    users = get_active_users()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return users


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserBase)
def show_one_user(user_id: str):
    '''
    Show one user in the platform
    '''
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.patch("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserBase)
def update_user_endpoint(user_id: str, new_user: UpdateUser):
    '''
    Update a user in the platform
    '''
    user = update_user(user_id, new_user)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: str):
    '''
    Delete a user in the platform
    '''
    if not delete_user(user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")