from fastapi import FastAPI
from app_17_4.routers import task, user

app=FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}


app.include_router(user.router)
app.include_router(task.router)


#uvicorn app_17_4.main:app --reload


#alembic init app_17_4/migrations                         #создать нужные файлы
#alembic revision --autogenerate -m "Initial migration"   #произвести миграцию
#alembic upgrade head                                     #создание таблиц task,user

