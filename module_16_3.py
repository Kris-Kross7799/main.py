from fastapi import FastAPI,FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users={'1': 'Имя: Зидан, возраст: 18',
       '2': 'Имя: Рональдо, возраст: 32',
       '3': 'Имя: Месси, возраст: 38'}

#возвращает словарь Users
@app.get("/users")
async def get_users():
    return users

#Создаём нового пользователя
@app.post("/users/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=3,
                                    max_length=30,
                                    description='Enter username',
                                    pattern="^[а-яА-Я0-9_-]+$",
                                    example='UrbanUser')],
        age: Annotated[int, Path(ge=18,
                                 le=110,
                                 description='Enter your age',
                                 example=77)]):
    new_id = str(int(max(users, key=int)) + 1)
    # new_user = {new_id: f"Имя: {username}, возраст: {age}"}
    # users[new_id]=f"Имя: {username}, возраст: {age}"
    users.update({new_id: f"Имя: {username}, возраст: {age}"})
    return f"User {new_id} is registered"


#обновляет значение словаря под заданным ключом
@app.put("/users/{user_id}/{username}/{age}")
async def update_user(user_id:Annotated[int, Path(ge=1,
                                 le=1000,
                                 description='Enter ID',
                                 example=77)],
                      username:Annotated[str, Path(min_length=3,
                                    max_length=30,
                                    description='Enter username',
                                    pattern="^[а-яА-Я0-9_-]+$",
                                    example='UrbanUser')],
                      age:Annotated[int, Path(ge=18,
                                 le=110,
                                 description='Enter your age',
                                 example=77)]):
    for key in users.keys():
        if key == str(user_id):
            users.update({user_id: f"Имя: {username}, возраст: {age}"})
            return f"The user {user_id} is updated"
    raise HTTPException(status_code=404, detail="пользователь с таким ID не найден")

#Удалить пользователя по ID
@app.delete("/users/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                 lt=1000,
                                 description='Enter ID',
                                 example=77)]):
    for id in list(users):
        if id == str(user_id):
            del users[id]
            return f"пользователь {user_id} удалён"
    raise HTTPException(status_code=404, detail="Пользователь с таким ID не найден")




#uvicorn module_16_3:app --reload