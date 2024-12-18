from fastapi import FastAPI, Path
from typing import Annotated

app=FastAPI()

@app.get('/')
async def get_main_page():
    return {'message': 'Главная страница!'}

@app.get('/user/admin')
async def hello_admin():
    return {'message': 'Вы вошли, как администратор'}

@app.get("/user/{user_id}")
async def get_user(
        user_id: Annotated[int, Path(gt=0,
                                     lt=100,
                                     description='Enter User ID',
                                     example=77)]):
    return {f"Вы вошли, как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_info(
        username:Annotated[str, Path(min_length=5,
                                     max_length=20,
                                     description="Enter username",
                                     example='UrbanUser')],
        age:Annotated[int, Path(gt=18,
                                lt=120,
                                description='Enter age',
                                example=24)]):
    return {f"message": f"Информация о пользователе: {username}, возраст {age}"}


# uvicorn module_16_2:app --reload