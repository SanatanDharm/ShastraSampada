#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12-03-2023 04:37 am
# @Author  : bhaskar.uprety
# @File    : auth

"""auth File created on 12-03-2023"""
import datetime
import uuid

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..utils import details_from_jwt, jwt_encode
from ...database.db import SessionLocal
from ...exceptions.user import InvalidLoginException, InvalidTokenException, NoUserException, UserNotVerifiedException
from ...models import BooleanResponse, UserCreate, UserResponse
from ...models.user import LogIn
from ...operations.database.user import UserOps
from ...operations.email import Emailer

emailer = Emailer('Shastra Sampada')
session = SessionLocal()

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@auth_router.post('/login')
async def login(data: LogIn) -> JSONResponse:
    """User Login"""
    try:
        user = UserOps(session, emailer, data.email)
        authentic = user.authenticate_user(data.password)
        if not user.verified:
            raise UserNotVerifiedException()
        if authentic:
            user_obj = user.get_user()
            token_key = uuid.uuid4().hex
            user.set_token(token_key)
            data = {
                'id': user_obj.id,
                'role': user_obj.role.name,
                'email': user_obj.email,
                'active': user_obj.active,
                'verified': user_obj.verified,
                'tocken_created': str(datetime.datetime.now()),
                'token_key': token_key
            }
            token = jwt_encode(data)

            content = {'detail': "Log in success", 'access_token': token, 'token_type': 'bearer'}
            headers = {'Authorization': f'Bearer {token}'}

            return JSONResponse(content, headers=headers)

        raise InvalidLoginException()
    except NoUserException:
        raise InvalidLoginException()


@auth_router.post('/signup', response_model=UserResponse)
def create_user(user: UserCreate):
    """Create one user"""
    u = UserOps(session, emailer)
    email = user.email
    password = user.password
    u.create(email=email, password=password)
    user = u.get_user()
    return user


@auth_router.get("/resend_verification/{email}", response_model=BooleanResponse)
def resend_verification(email: str):
    """Resend verification email"""
    u = UserOps(session, emailer, email)
    sent: bool = u.resend_verification()
    return {
        'success': sent,
        'message': "Verification email sent"
    }


@auth_router.post("/verify_account/{email}/{token}", response_model=BooleanResponse)
def verify_account(email: str, token: str):
    """Verify account"""
    u = UserOps(session, emailer, email)
    verified: bool = u.verify_account(token)

    return {
        'success': verified,
        'message': "Account verified"
    }


@auth_router.get('/profile', response_model=UserResponse)
async def my_profile(jwt_details=Depends(details_from_jwt)):
    """Get current user"""
    try:
        u = UserOps(session, emailer, jwt_details['email'])
        u.validate_token(jwt_details)
        user = u.get_user()
        return user
    except NoUserException:
        raise InvalidTokenException()


@auth_router.post('/logout', response_model=BooleanResponse)
async def log_out(jwt_details=Depends(details_from_jwt)):
    """Get current user"""
    try:
        u = UserOps(session, emailer, jwt_details['email'])
        u.validate_token(jwt_details)
        u.remove_token()

        return {
            'success': True,
            'message': "Logout success"
        }
    except NoUserException:
        raise InvalidTokenException()
