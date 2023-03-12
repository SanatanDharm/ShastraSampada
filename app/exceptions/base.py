#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12-03-2023 08:34 am
# @Author  : bhaskar.uprety
# @File    : base

"""base File created on 12-03-2023"""
from fastapi import HTTPException, status


class BaseHTTPException(HTTPException):
    """Base HTTP Exception"""
    _status = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Something went wrong'

    def __init__(self):
        super().__init__(self._status, detail=self.message)
