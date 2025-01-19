from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app_17_5.backend.db_depends import get_db
from typing import Annotated
from app_17_5.schemas.user import CreateUser, User, UpdateUser
from app_17_5.schemas.task import CreateTask, Task
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


# Фейковые данные
# users = [{"id": 1, "name": 'Petr'}, {'id': 2, 'name': 'Egor'}]

# -------------------------------------------------------------------------------
@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User).where(User.is_active == True)).all()
    return users


# -------------------------------------------------------------------------------
# @router.get('/user_id')
# async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
#     user = db.scalar(select(User).where(User.id == user_id))
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
#
#     return user
# ------------------------------------------------------------------------------
@router.get('/user_id/tasks')
async def tasks_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user=db.scalar(select(User).where(User.id == user_id))
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
        # if tasks is None:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tasks were not found')
    return tasks
# ------------------------------------------------------------------------------
@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()  # коммит изменений в БД
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}


# -------------------------------------------------------------------------------
@router.put('/update_user')
def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User was not found')

    db.execute(update(User).where(User.id == user_id).values(username=update_user.username,
                                                             firstname=update_user.firstname,
                                                             lastname=update_user.lastname,
                                                             age=update_user.age,
                                                             slug=slugify(update_user.username)))

    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User update is successful'}

# -------------------------------------------------------------------------------
@router.delete('/delete')
def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found')

    # db.execute(update(User).where(User.id == user_id).values(is_active=False))
    db.execute(delete(User).where(User.id == user_id))
    db.execute(delete(Task).where(Task.user_id == user_id))

    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User delete is successful'}
