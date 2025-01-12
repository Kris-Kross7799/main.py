from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session
from app_17_4.backend.db_depends import get_db
from typing import Annotated
from app_17_4.schemas.task import CreateTask, Task
from sqlalchemy import insert, select, update

router = APIRouter(prefix='/task', tags=['task'])


# Фейковые данные
# products = [{"id": 1, "name": 'Laptop', 'user_id': 1}, {'id': 2, 'name': 'Book', 'user_id': 2}]


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.is_active == True)).all()
    if tasks is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no task'
        )
    return tasks


# @router.get('/user_id')
# async def task_by_user(db: Annotated[Session, Depends(get_db)], user_id: int):
#     user = db.scalar(select(User).where(User.id == user_id))
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail='User not found'
#         )
#     subcategories = db.scalars(select(Category).where(Category.parent_id == category.id)).all()
#     categories_and_subcategories = [category.id] + [i.id for i in subcategories]
#     task_user = db.scalars(
#         select(Task).where(Task.category_id.in_(categories_and_subcategories), Product.is_active == True,
#                               Product.stock > 0)).all()
#     return products_category

#
# @router.get('/detail/{product_slug}')
# async def product_detail(db: Annotated[Session, Depends(get_db)], product_slug: str):
#     product = db.scalar(
#         select(Product).where(Product.slug == product_slug, Product.is_active == True, Product.stock > 0))
#     if not product:
#         return HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail='There are no product'
#         )
#     return product


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask):
    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   user_id=create_task.user_id))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/task_id')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: str,
                      update_task_model: CreateTask):
    task_update = db.scalar(select(Task).where(Task.id == task_id))
    if task_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no task found'
        )

    db.execute(update(Task).where(Task.slug == task_id)
               .values(title=update_task_model.title,
                       content=update_task_model.content,
                       priority=update_task_model.priority,
                       user_id=update_task_model.user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful'
    }
