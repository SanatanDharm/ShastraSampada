#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04-03-2023 01:04 pm
# @Author  : bhaskar.uprety
# @File    : enum

"""enum File created on 04-03-2023"""
from enum import Enum


class ReviewStatus:
    """review status enumeration"""
    IN_PROGRESS = 'in_progress'
    APPROVED = 'approved'
    REJECTED = 'rejected'


class ContentRequestStatus:
    """content request status enumeration"""
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'


class Role(str, Enum):
    """role model"""
    user = 1
    operator = 2
    expert = 3
    moderator = 4
    admin = 5
