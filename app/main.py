#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 08:32 am
# @Author  : bhaskar.uprety
# @File    : main.py

"""main.py File created on 04-03-2023"""
from typing import List

from fastapi import FastAPI, HTTPException, status

from .database.db import Base, SessionLocal, engine
from .database.models.user import User
from .models import UserCreate, UserResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency
db = SessionLocal()


# User routes
@app.get("/users", response_model=List[UserResponse])
def get_all_users():
    return db.query(User).all()


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    get_user = db.query(User).filter(User.email == user.email).first()
    if get_user:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, 'User already exists')
    email = user.email
    password = user.password
    user = User(email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
#
#
# @app.patch("/users/{user_id}/role")
# def set_user_role(user_id: int, role_id: int):
#     user = db.query(User).filter(id=user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     role = db.query(Role).filter(Role.id == role_id).first()
#     if not role:
#         raise HTTPException(status_code=404, detail="Role not found")
#     user.role = role
#     db.commit()
#     db.refresh(user)
#     return user
