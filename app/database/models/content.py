#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 01:00 pm
# @Author  : bhaskar.uprety
# @File    : content

"""content File created on 04-03-2023"""
import time

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base


class Book(Base):
    """book model"""
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String)

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)
    chapters = relationship('Chapter', back_populates='book')


class Chapter(Base):
    """chapter model"""
    __tablename__ = 'chapter'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='chapters')
    paragraphs = relationship('Paragraph', back_populates='chapter')

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)


class Paragraph(Base):
    """paragraph model"""
    __tablename__ = 'paragraph'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    chapter_id = Column(Integer, ForeignKey('chapter.id'))
    chapter = relationship('Chapter', back_populates='paragraphs')
    images = relationship('Image', back_populates='paragraph')
    translations = relationship('Translation', back_populates='paragraph')
    error_reports = relationship('ErrorReport', back_populates='paragraph')

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)


class Translation(Base):
    """translation model"""
    __tablename__ = 'translation'

    id = Column(Integer, primary_key=True)
    language = Column(String, nullable=False)
    content = Column(String)
    paragraph_id = Column(Integer, ForeignKey('paragraph.id'))
    paragraph = relationship('Paragraph', back_populates='translations')

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)


class Image(Base):
    """image model"""
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    paragraph_id = Column(Integer, ForeignKey('paragraph.id'))
    paragraph = relationship('Paragraph', back_populates='images')

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)
