#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11-03-2023 09:48 am
# @Author  : bhaskar.uprety
# @File    : user.py

"""user.py File created on 11-03-2023"""
from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .base import BaseOps
from ..email import Emailer
from ..utils import generate_random_number
from ...database.enum import Role
from ...database.models import User
from ...exceptions.user import (
    DuplicateUserException, InvalidLoginException, NoUserException,
    UserReVerificationException
)


class UserOps(BaseOps):
    """User operations"""

    def __init__(self, session: Session, emailer: Emailer, email: str = None):
        super().__init__(session)
        self.email = email
        self.emailer = emailer

    def create(self, email: str, password: str):
        """Create a user"""
        try:
            varification_token = self.get_token()
            hashed_token = self.create_hash(varification_token)
            hashed_password = self.create_hash(password)
            user = User(email=email, password=hashed_password, verification_key=hashed_token)
            self.commit(user)
            self.email = email
            self.emailer.send_verification_email(email, varification_token)
        except IntegrityError:
            raise DuplicateUserException()

    def resend_verification(self):
        """Resend verification email"""
        user = self.get_user()
        verified = user.verified
        if not verified:
            varification_token = self.get_token()
            user.verification_key = self.create_hash(varification_token)
            self.emailer.send_verification_email(self.email, varification_token)
            self.commit(user)
            return {'details': 'Verification email sent'}
        raise UserReVerificationException()

    def verify_account(self, raw_token):
        """Verify token"""
        user = self.get_user()
        verified = user.verified
        if not verified:
            hashed_token = user.verification_key
            verified = self.compare_hash(raw_token, hashed_token)
            if verified:
                user.verified = True
                user.verification_key = None
                self.commit(user)
            else:
                raise InvalidLoginException()

            return {'details': 'Verification successfull'}

        raise UserReVerificationException()

    def get_user(self):
        """Get one user"""
        user = self.session.query(User).filter_by(email=self.email).first()
        if user:
            return user
        raise NoUserException()

    def set_role(self, role: Role):
        """Set the given role"""
        user = self.get_user()
        user.role = role
        self.commit(user)
        return user

    def authenticate_user(self, password: str):
        """Authenticate user"""
        user = self.session.query(User).filter_by(email=self.email).first()
        hashed_pwd: str = user.password

        success = self.compare_hash(password, hashed_pwd)
        return success

    @property
    def verified(self) -> bool:
        """Check if user is verified"""
        user = self.session.query(User).filter_by(email=self.email).first()
        return user.verified

    @staticmethod
    def get_token() -> str:
        """Create a verification token"""
        random_number = generate_random_number(6)
        return str(random_number)

    @staticmethod
    def create_hash(row_str):
        """Hash given password"""
        row_bytes = row_str.encode('utf-8')
        salt = gensalt()
        hashed_bytes = hashpw(row_bytes, salt)
        hashed_str = hashed_bytes.decode()
        return hashed_str

    @staticmethod
    def compare_hash(row_str, hashed_str):
        """Compare given password"""
        row_bytes = row_str.encode('utf-8')
        hashed_bytes = hashed_str.encode()

        success = checkpw(row_bytes, hashed_bytes)
        return success
