#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 08:31 am
# @Author  : bhaskar.uprety
# @File    : __init__.py

"""__init__.py File created on 04-03-2023"""
import datetime
import time
from typing import Optional

# Models for request and response bodies
from pydantic import BaseModel


class RoleCreate(BaseModel):
    name: str


class UserCreate(BaseModel):
    email: str
    password: str
    role_id: Optional[int]


class UserResponse(BaseModel):
    id: int
    email: str
    role_id: Optional[int]
    active: bool
    suspended: bool
    level: int
    verified: bool
    created_at: float

    class Config:
        orm_mode = True
        exclude = ['password', 'updated_at']
