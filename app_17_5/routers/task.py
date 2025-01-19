from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session
from app_17_5.backend.db_depends import get_db
from typing import Annotated
from app_17_5.schemas.task import CreateTask, Task
from app_17_5.schemas.user import User
from sqlalchemy import insert, select, update, delete

router = APIRouter(prefix='/task', tags=['task'])


# Фейковые данные
# products = [{"id": 1, "name": 'Laptop', 'user_id': 1}, {'id': 2, 'name': 'Book', 'user_id': 2}]


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.is_active == True)).all()
    return tasks


# -------------------------------------------------------------------------------
@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
    return task


# @router.get('/user_id')
# async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
#     user = db.scalar(select(User).where(User.id == user_id))
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
#
#     return user
# -------------------------------------------------------------------------------
@router.post('/user_id')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, create_task: CreateTask):
    userid = db.scalar(select(User).where(User.id == user_id))
    if userid is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User was not found')

    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   user_id=create_task.user_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Task create successful'}


# -------------------------------------------------------------------------------
@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: str,
                      update_task: CreateTask):
    task_update = db.scalar(select(Task).where(Task.id == task_id))
    if task_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There is no task found')
    db.execute(update(Task).where(Task.id == task_id).values(title=update_task.title,
                                                         content=update_task.content,
                                                         priority=update_task.priority,
                                                         user_id=update_task.user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful'}


# @router.put('/update_user')
# def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
#     user = db.scalar(select(User).where(User.id == user_id))
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail='User was not found')
#
#     db.execute(update(User).where(User.id == user_id).values(username=update_user.username,
#                                                              firstname=update_user.firstname,
#                                                              lastname=update_user.lastname,
#                                                              age=update_user.age,
#                                                              slug=slugify(update_user.username)))
#
#     db.commit()
#     return {'status_code': status.HTTP_200_OK,
#             'transaction': 'User update is successful'}
# -------------------------------------------------------------------------------
@router.delete('/delete')
def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found')

    # db.execute(update(User).where(User.id == user_id).values(is_active=False))
    db.execute(delete(Task).where(Task.id == task_id))

    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Task delete is successful'}
