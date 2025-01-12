from pydantic import BaseModel, Field
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app_17_4.backend.db import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    task = relationship('Task', back_populates='user')
    # task = relationship('app_17_4.schemas.Task', back_populates='user')


class CreateUser(BaseModel):
    username: str=Field(..., min_length=3,
                          max_length=30,
                          pattern="^[а-яА-ЯёЁa-zA-Z0-9]+$",
                          description='ник пользователя')
    firstname: str=Field(..., min_length=3,
                          max_length=30,
                          pattern="^[а-яА-ЯёЁa-zA-Z0-9]+$",
                          description='имя пользователя')
    lastname: str=Field(..., min_length=3,
                          max_length=30,
                          pattern="^[а-яА-ЯёЁa-zA-Z0-9]+$",
                          description='фамилия пользователя')
    age: int=Field(..., ge=18,
                     le=110,
                     description='Введите возраст',
                     example=77)


class UpdateUser(BaseModel):
    username: str = Field(..., min_length=3,
                          max_length=30,
                          pattern="^[а-яА-ЯёЁa-zA-Z0-9]+$",
                          description='имя пользователя')
    firstname: str = Field(..., min_length=3,
                           max_length=30,
                           pattern="^[а-яА-ЯёЁa-zA-Z0-9]+$",
                           description='имя пользователя')
    lastname: str = Field(..., min_length=3,
                          max_length=30,
                          pattern="^[а-яА-ЯёЁa-zA-Z0-9]+$",
                          description='имя пользователя')
    age: int = Field(..., ge=18,
                     le=110,
                     description='Введите возраст',
                     example=77)


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
