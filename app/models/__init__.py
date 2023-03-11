#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 08:31 am
# @Author  : bhaskar.uprety
# @File    : __init__.py

"""__init__.py File created on 04-03-2023"""
from typing import Optional

# Models for request and response bodies
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """User creation model"""
    email: EmailStr
    password: str
    role_id: Optional[int]


class UserResponse(BaseModel):
    """User response model"""
    id: int
    email: EmailStr
    role_id: Optional[int]
    active: bool
    suspended: bool
    level: int
    verified: bool

    class Config:
        """Configuration"""
        orm_mode = True
        exclude = ['password', 'updated_at', 'verification_key', 'created_at']
