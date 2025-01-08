from fastapi import FastAPI
from aplication.models import task, user

app=FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}


app.include_router(user.router)
app.include_router(task.router)


#python -m uvicorn application.main:application
#uvicorn main:app --host 0.0.0.0 --reload

#uvicorn main:app --reload