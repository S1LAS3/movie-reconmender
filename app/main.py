from fastapi import FastAPI

app = FastAPI()

from app.services.db_services import get_users, create_user

@app.get("/users")
def list_users():
    return get_users()

@app.post("/users")
def  add_users(name: str):
    create_user(name)
    return{"msg":"usuário criado"}