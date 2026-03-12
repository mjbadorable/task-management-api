import os

from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TasksCreate(BaseModel):
    title: str

class Task(BaseModel):
    id: int
    title: str
    completed: bool
    class Config:
        from_attributes = True