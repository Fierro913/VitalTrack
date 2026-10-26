from fastapi import FastAPI
from routers import user
from data.user import initialize_csv

app = FastAPI()


def create_db_tables():
    pass


@app.on_event("startup")
def on_startup():
    initialize_csv()
app.include_router(router=user.router, prefix="/users", tags=["users"])