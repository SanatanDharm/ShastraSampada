#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 01:51 pm
# @Author  : bhaskar.uprety
# @File    : log

"""log File created on 04-03-2023"""
import time

from sqlalchemy import Column, Float, ForeignKey, Integer, String

from ..db import Base


class AuditLog(Base):
    """Audit log"""
    __tablename__ = 'audit_log'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    action = Column(String(100), nullable=False)
    created_at = Column(Float, default=time.time)