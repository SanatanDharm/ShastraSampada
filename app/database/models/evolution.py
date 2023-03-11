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


class BaseReview(Base):
    """Base review model"""
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)


class ExpertReview(BaseReview):
    """review model"""
    __tablename__ = 'expert_review'

    paragraph_id = Column(Integer, ForeignKey('paragraph.id'))
    paragraph = relationship('Paragraph', back_populates='reviews')
    user = relationship('User', back_populates='validations')


class BookReview(BaseReview):
    """book review model"""
    __tablename__ = 'book_review'

    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='reviews')
    user = relationship('User', back_populates='reviews')
