#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12-03-2023 08:34 am
# @Author  : bhaskar.uprety
# @File    : user

"""user File created on 12-03-2023"""
from starlette import status

from .base import BaseHTTPException


class NotLoggedinException(BaseHTTPException):
    """User is not found"""
    _status = status.HTTP_403_FORBIDDEN
    message = 'Login to continueue'


class NoUserException(BaseHTTPException):
    """User is not found"""
    _status = status.HTTP_404_NOT_FOUND
    message = 'User not found'


class DuplicateUserException(BaseHTTPException):
    """User is not found"""
    _status = status.HTTP_306_RESERVED
    message = 'User already exist'


class UserReVerificationException(BaseHTTPException):
    """User is not found"""
    _status = status.HTTP_304_NOT_MODIFIED
    message = 'User is already verified'


class UserNotVerifiedException(BaseHTTPException):
    """User is not found"""
    _status = status.HTTP_403_FORBIDDEN
    message = 'Verify your account first'


class InvalidTokenException(BaseHTTPException):
    """User is not found"""
    _status = status.HTTP_401_UNAUTHORIZED
    message = 'Invalid varification token'


class InvalidLoginException(BaseHTTPException):
    """User is not found"""
    _status = status.HTTP_401_UNAUTHORIZED
    message = 'Invalid username or password'


class ExpiredTokenException(BaseHTTPException):
    """User is not found"""
    _status = status.HTTP_406_NOT_ACCEPTABLE
    message = 'Expired varification token'
