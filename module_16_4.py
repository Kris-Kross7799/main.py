from fastapi import FastAPI, FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = [
    User(id=1, username='Зидан', age=18),
    User(id=2, username='Рональдо', age=32),
    User(id=3, username='Месси', age=38)]


# возвращает список Users
@app.get("/users", response_model=List[User])
async def get_users():
    return users


class CreateUser(BaseModel):  # Создать нового пользователя
    username: str = Field(..., min_length=3,
                          max_length=30,
                          pattern="^[а-яА-ЯёЁa-zA-Z0-9]+$",
                          description='имя пользователя')
    age: int = Field(..., ge=18,
                     le=110,
                     description='Введите возраст',
                     example=77)


# Создаём нового пользователя
@app.post("/users", response_model=User)
async def create_user(user: CreateUser):
    new_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user


# обновляет значение словаря под заданным ключом
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: CreateUser):
    for u in users:
        if u.id == user_id:
            u.username = user.username
            u.age = user.age
            return u
    raise HTTPException(status_code=404, detail="пользователь с таким ID не найден")


# Удалить пользователя по ID
@app.delete("/users/{user_id}", response_model=str)
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return f'Пользователь {user_id} удалён'
    raise HTTPException(status_code=404, detail="Пользователь с таким ID не найден")

# uvicorn module_16_4:app --reload
