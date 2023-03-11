#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11-03-2023 10:09 am
# @Author  : bhaskar.uprety
# @File    : base

"""base File created on 11-03-2023"""
from abc import ABC

from sqlalchemy.orm import Session


class BaseOps(ABC):
    """User operations"""

    def __init__(self, session: Session):
        self.session = session

    def commit(self, obj):
        """Create a user"""
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
