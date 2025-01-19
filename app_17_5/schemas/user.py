from pydantic import BaseModel, Field
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app_17_5.backend.db import Base


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
    # task = relationship('app_17_5.schemas.Task', back_populates='user')


class CreateUser(BaseModel):
    # username: str = Field(..., min_length=3,
    #                       max_length=30,
    #                       pattern="^[а-яА-Яa-zA-Z0-9\\s?!,.'Ёё]+$",
    #                       description='ник пользователя',
    #                       example='User')
    # firstname: str = Field(..., min_length=3,
    #                        max_length=30,
    #                        pattern="^[а-яА-Яa-zA-Z0-9\\s?!,.'Ёё]+$",
    #                        description='имя пользователя',
    #                        example='Alex')
    # lastname: str = Field(..., min_length=3,
    #                       max_length=30,
    #                       pattern="^[а-яА-Яa-zA-Z0-9\\s?!,.'Ёё]+$",
    #                       description='фамилия пользователя',
    #                       example='Beloff')
    # age: int = Field(..., ge=18,
    #                  le=110,
    #                  description='Введите возраст',
    #                  example=77)
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(BaseModel):
    # username: str = Field(..., min_length=3,
    #                       max_length=30,
    #                       pattern="^[а-яА-Яa-zA-Z0-9\\s?!,.'Ёё]+$",
    #                       description='ник пользователя',
    #                       example='User')
    # firstname: str = Field(..., min_length=3,
    #                        max_length=30,
    #                        pattern="^[а-яА-Яa-zA-Z0-9\\s?!,.'Ёё]+$",
    #                        description='имя пользователя',
    #                        example='Alex')
    # lastname: str = Field(..., min_length=3,
    #                       max_length=30,
    #                       pattern="^[а-яА-Яa-zA-Z0-9\\s?!,.'Ёё]+$",
    #                       description='фамилия пользователя',
    #                       example='Beloff')
    # age: int = Field(..., ge=18,
    #                  le=110,
    #                  description='Введите возраст',
    #                  example=55)
    username: str
    firstname: str
    lastname: str
    age: int


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
