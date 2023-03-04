#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 01:02 pm
# @Author  : bhaskar.uprety
# @File    : evolution

"""evolution File created on 04-03-2023"""
import time

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base


class Review(Base):
    """review model"""
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    paragraph_id = Column(Integer, ForeignKey('paragraph.id'))
    paragraph = relationship('Paragraph')

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)
