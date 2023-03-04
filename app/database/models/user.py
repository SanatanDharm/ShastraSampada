#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 12:58 pm
# @Author  : bhaskar.uprety
# @File    : user

"""user File created on 04-03-2023"""
import time

from sqlalchemy import Boolean, Column, Enum, Float, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base
from ..enum import Role


class User(Base):
    """
    user model
    we can consider level as amount of accessable feature
    e.g. 1 is guest, 2 is a regular user, 3 is a user who can comment
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    level = Column(Integer, nullable=False, default=1)

    role = Column(Enum(Role), default=Role.user, nullable=False)
    error_reports = relationship('ErrorReport', back_populates='user')

    active = Column(Boolean, default=True)
    verified = Column(Boolean, default=False)
    suspended = Column(Boolean, default=False)

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)
