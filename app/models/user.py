#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12-03-2023 04:56 am
# @Author  : bhaskar.uprety
# @File    : user

"""user File created on 12-03-2023"""
from pydantic import BaseModel, EmailStr


class LogIn(BaseModel):
    """Login Model"""
    email: EmailStr
    password: str
