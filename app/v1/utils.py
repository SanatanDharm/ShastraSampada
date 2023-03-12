#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12-03-2023 05:38 am
# @Author  : bhaskar.uprety
# @File    : utils

"""utils File created on 12-03-2023"""
import os

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import ExpiredSignatureError, InvalidSignatureError

from app.exceptions.user import ExpiredTokenException, InvalidTokenException, NotLoggedinException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='v1/auth/login')
__secret = os.environ.get('JWT_SECRET_KEY')


def jwt_encode(details):
    """Encode JWT"""
    token = jwt.encode(details, __secret, algorithm="HS256")

    return token


def jwt_decode(token):
    """Encode JWT"""
    details = jwt.decode(token, __secret, algorithms="HS256")

    return details


def get_user_from_jwt(token: str = Depends(oauth2_scheme)) -> dict:
    """Get user from JWT"""
    try:
        details = jwt_decode(token)
        return details
    except ExpiredSignatureError:
        raise ExpiredTokenException()
    except InvalidSignatureError:
        raise InvalidTokenException()
    except Exception:
        raise NotLoggedinException()
