# from fastapi import FastAPI
# Создаем экземпляр приложения FastAPI
# app = FastAPI()
# Определение базового маршрута
@app.get("/")
async def root():
    return {"message": "Hoho, UrbanStuden!"}

@app.get("/user/A/B")
async def news():
    return {"message": f"Hello, TESTER!"}

@app.get("/user/{first_name}/{last_name}") #{}-слаги
async def news(first_name:str,last_name:str):
    return {"message": f"Hi, {first_name} {last_name}"}



#Примеры основных запросов
#GET-запрос — получение данных:
@app.get("/items/")
async def read_items(skip: int=0,limit:int=10)->dict:
    items=[{'item_id':i} for i in range(skip,skip+limit)]
    return {"items": items}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}")
async def get_user(user_id: int)->dict:
    return {"user_id": user_id, 'name':f"User{user_id}"}

#Совмещение динамических параметров и параметров запроса
@app.get("/products/{product_id}")
async def read_product(product_id: int, details: bool = False) -> dict:
    product_info = {"product_id": product_id, "name": f"Product {product_id}"}
    if details:
        product_info["details"] = "Detailed product information"
    return product_info

#product_id — это динамический параметр URL, а details — параметр запроса.
# Если details установлен в True, возвращается доп. информация о продукте.

@app.get("/id")
async def id_paginator(username:str='Alex',age:int=24)->dict:
    return {"User": username, "Age":age}

#Пример с пересечением маршрутов (Рис.11, 12)
# Рассмотрим два маршрута:
@app.get("/items/new") #возвращает сообщение о новых элементах.
async def read_new_items() -> dict:
    return {"message": "This is a list of new items"}

@app.get("/items/{item_id}") #предназначен для получения элемента по ID
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "name": f"Item {item_id}"}

#Пример маршрута с несколькими параметрами
@app.get("/categories/{category_id}/items/{item_id}")
async def read_category_item(category_id: int, item_id: int) -> dict:
    return {"category_id": category_id, "item_id": item_id}

#Обработка путей с фиксированными и динамическими частями
@app.get("/users/me") #возвращает информацию о текущем пользователе
async def read_current_user() -> dict:
    return {"user": "This is the current user"}

@app.get("/users/{user_id}") #возвращает информацию о пользователе по ID
async def read_user(user_id: int) -> dict:
    return {"user_id": user_id, "name": f"User {user_id}"}
#Совет: Фиксированные пути (такие как /users/me) всегда должны быть
# определены до динамических путей (таких как /users/{user_id})




# POST-запрос — добавление данных:
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: float
@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

# UT-запрос — обновление данных:
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

# DELETE-запрос — удаление данных:
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}

@app.post("/products/")
async def create_product():
#Создает новый продукт в системе.
# - **name**: название продукта
# - **price**: цена продукта
# - **quantity**: количество на складе
    return

#uvicorn main:app --reload
#python -m uvicorn main:app