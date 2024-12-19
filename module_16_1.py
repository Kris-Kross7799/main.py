from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def get_main_page():
    return 'Главная страница!'

@app.get('/user/admin')
async def hello_admin():
    return 'Вы вошли, как администратор'

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return f"Вы вошли, как пользователь № {user_id}"

@app.get("/user")
async def user_info(username:str="Georg",age:str=37):
    return f"Информация о пользователе: {username}, возраст {age}"


# uvicorn module_16_1:app --reload