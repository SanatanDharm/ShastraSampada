#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 08:37 am
# @Author  : bhaskar.uprety
# @File    : db.py

"""db.py File created on 04-03-2023"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create engine
engine = create_engine('sqlite:///shastrasampada.db')

# create base
Base = declarative_base()
SessionLocal = sessionmaker(autoflush=False, bind=engine)
