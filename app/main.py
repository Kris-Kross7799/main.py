from fastapi import FastAPI
from routers import category

app=FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'my shop'}

app.include_router(category.router)

#python -m uvicorn main:app


