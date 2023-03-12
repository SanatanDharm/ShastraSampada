#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12-03-2023 04:46 am
# @Author  : bhaskar.uprety
# @File    : core

"""core File created on 12-03-2023"""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt import JwtAuthorizationCredentials

from .v1 import api_v1


class App(FastAPI):
    """Custom fastapi App"""
    Credentials = JwtAuthorizationCredentials


app = App(
    docs_url="/",
    # redoc_url=None,
    version=os.environ.get('VERSION'),
    title="Shastra Shampada",
    description="""Unlock the wisdom of the ages with Shastra Shampada - Your gateway to the world of Hinduism""",
    contact={
        "name": "Rudransh Jagannath",
        "email": "JRudransh@protonmail.com",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.mount('/v1', api_v1)
