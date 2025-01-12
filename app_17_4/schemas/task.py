from pydantic import BaseModel
from fastapi import APIRouter
from app_17_4.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship




class Task(Base):
    __tablename__='tasks'
    __table_args__ = {'keep_existing':True}
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String)
    content=Column(String)
    priority=Column(Integer, default=0)
    completed=Column(Boolean, default=False)
    user_id=Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug=Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)


    user=relationship('User',back_populates='task')
    # user=relationship('app_17_4.schemas.User',back_populates='task')

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Task.__table__))



class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int


