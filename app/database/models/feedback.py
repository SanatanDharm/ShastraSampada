#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 01:02 pm
# @Author  : bhaskar.uprety
# @File    : feedback

"""feedback File created on 04-03-2023"""
import time

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Text, VARCHAR
from sqlalchemy.orm import relationship

from ..db import Base


class ErrorReport(Base):
    """error report model"""
    __tablename__ = 'error_report'

    id = Column(Integer, primary_key=True)
    content_table = Column(VARCHAR)
    content_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    error_type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_resolved = Column(Boolean, default=False)

    paragraph_id = Column(Integer, ForeignKey('paragraph.id'))
    paragraph = relationship('Paragraph', back_populates='error_reports')
    user = relationship('User', back_populates='error_reports')

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)


class ContentRequest(Base):
    """New content request"""
    __tablename__ = 'content_request'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)
