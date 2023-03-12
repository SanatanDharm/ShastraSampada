#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 08:32 am
# @Author  : bhaskar.uprety
# @File    : main.py

"""main.py File created on 04-03-2023"""
from dotenv import load_dotenv

load_dotenv()  # noqa

from .core import app
from .database.db import Base, engine

Base.metadata.create_all(bind=engine)


@app.get("/live")
def check_live():
    """Check Live Status"""
    return True
