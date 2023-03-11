#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 08:32 am
# @Author  : bhaskar.uprety
# @File    : main.py

"""main.py File created on 04-03-2023"""

from dotenv import load_dotenv
from fastapi import FastAPI

from .database.db import Base, SessionLocal, engine
from .models import UserCreate, UserResponse
from .operations.database.user import UserOps
from .operations.email import Emailer

load_dotenv()
app = FastAPI()
emailer = Emailer('Shastra Sampada')

Base.metadata.create_all(bind=engine)

# Dependency
session = SessionLocal()


# User routes
@app.get("/users/{email}", response_model=UserResponse)
def get_one_users(email: str):
    """Get one user"""
    u = UserOps(session, emailer, email)
    return u.get_user()


@app.get("/resend_verification/{email}")
def resend_verification(email: str):
    """Get one user"""
    u = UserOps(session, emailer, email)
    return u.resend_verification()


@app.post("/verify_account/{email}/{token}")
def verify_account(email: str, token: str):
    """Get one user"""
    u = UserOps(session, emailer, email)
    return u.verify_account(token)


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    """Create one user"""
    u = UserOps(session, emailer)
    email = user.email
    password = user.password
    u.create(email=email, password=password)
    user = u.get_user()
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
