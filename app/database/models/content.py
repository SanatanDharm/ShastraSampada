#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 01:00 pm
# @Author  : bhaskar.uprety
# @File    : content

"""content File created on 04-03-2023"""
import time

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, VARCHAR
from sqlalchemy.orm import relationship

from ..db import Base


class BaseContent(Base):
    """Base class for all content"""
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR, nullable=False)
    description = Column(String, nullable=False)

    created_at = Column(Float, default=time.time)
    updated_at = Column(Float, default=time.time, onupdate=time.time)


class Book(BaseContent):
    """book model"""
    __tablename__ = 'book'

    origin = Column(VARCHAR, nullable=False)
    chapters = relationship('Chapter', back_populates='book')
    chapter_title = Column(VARCHAR, nullable=False)
    reviews = relationship('BookReview', back_populates='book')


class Chapter(BaseContent):
    """chapter model"""
    __tablename__ = 'chapter'

    content = Column(String)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('Book', back_populates='chapters')
    paragraphs = relationship('Paragraph', back_populates='chapter')
    paragraphs_title = Column(VARCHAR, nullable=False)


class Paragraph(BaseContent):
    """paragraph model"""
    __tablename__ = 'paragraph'

    content = Column(String)
    chapter_id = Column(Integer, ForeignKey('chapter.id'))
    chapter = relationship('Chapter', back_populates='paragraphs')
    # images = relationship('Image', back_populates='paragraph')
    translations = relationship('Translation', back_populates='paragraph')
    error_reports = relationship('ErrorReport', back_populates='paragraph')
    reviews = relationship('ExpertReview', back_populates='paragraph')


# class Image(BaseContent):
#     """image model"""
#     __tablename__ = 'image'
#
#     url = Column(String, nullable=False)
#     paragraph = relationship('Paragraph', back_populates='images')


class Language(Base):
    """Audit log"""
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True)
    action = Column(String(100), nullable=False)
    created_at = Column(Float, default=time.time)

    translations = relationship('Translation', back_populates='language')


class Translation(BaseContent):
    """translation model"""
    __tablename__ = 'translation'

    language_id = Column(Integer, ForeignKey('language.id'), nullable=False)
    language = relationship('Language', back_populates='translations')
    content = Column(String)
    paragraph_id = Column(Integer, ForeignKey('paragraph.id'))
    paragraph = relationship('Paragraph', back_populates='translations')

    published = Column(Boolean, default=False)
    checked = Column(Boolean, default=False)
