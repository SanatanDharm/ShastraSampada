#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12-03-2023 05:25 am
# @Author  : bhaskar.uprety
# @File    : app

"""app File created on 12-03-2023"""
from fastapi import FastAPI

from .routes.auth import auth_router

api_v1 = FastAPI(
    docs_url='/'
)

api_v1.include_router(auth_router)
