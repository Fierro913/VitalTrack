from fastapi import APIRouter, status, HTTPException
from models.user import userbase, updateuser

users_list:list[userbase] = []

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(new_user: userbase):
    '''
    Create a new user in the platform
    :param new_user:
    :return: OK, Created with status 201
    '''
    users_list.append(new_user)
    return {"New User Added": new_user}


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[userbase])
def show_all_users():
    '''
    Show all users in the platform
    :return: List with whole users registered
    '''
    if users_list:
        return users_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users found")

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=userbase)
def show_one_user(user_id: str):
    '''
    Show one user in the platform
    :param user_id:
    :return: A user with the same ID registered
    '''
    if not users_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users found")
    elif len(users_list)<user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found for list size")
    else:
        for user in users_list:
            if user.id == user_id:
                return user
        return "User not found"


@router.patch("/{user_id}", status_code=status.HTTP_200_OK, response_model=userbase)
def update_user(user_id: str, new_user: updateuser):
    '''
    Update a user in the platform
    :param user_id:
    :param new_user:
    :return: the new name of the user
    '''
    if not users_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users found")
    else:
        for user in users_list:
            if user.id == user_id:
                user.name = new_user.name
                return user
        return None


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    if users_list:
        for user in users_list:
            if user.id == user_id:
                users_list.remove(user)
                return user
            return "User not found"
        return "User not found"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users found")