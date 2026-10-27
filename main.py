from fastapi import FastAPI
from routers import user, food, glucose_register
from data.user import initialize_csv as init_users
from data.food import initialize_csv as init_foods
from data.glucose_register import initialize_csv as init_registers

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_users()
    init_foods()
    init_registers()


app.include_router(router=user.router, prefix="/users", tags=["users"])
app.include_router(router=food.router, prefix="/foods", tags=["foods"])
app.include_router(router=glucose_register.router, prefix="/glucose", tags=["glucose"])