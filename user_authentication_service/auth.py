#!/usr/bin/env python3
""" Auth
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ hash password
    """
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    return hash


def _generate_uuid() -> str:
    """ Generate uuid
    """
    myuuid = uuid.uuid4()
    return str(myuuid)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hash_password = _hash_password(password)
            user = self._db.add_user(email, hash_password)
            return user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """ valid user email and password
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode("utf-8"), user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ return session id
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ return user by session_id
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy session by user_id
        """

        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ reset password
        """
        try:
            user = self._db.find_user_by(email=email)

            reset_token = _generate_uuid()

            self._db.update_user(user.id, reset_token=reset_token)

            return reset_token

        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            h_pww = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=h_pww, reset_token=None)
        except NoResultFound:
            raise ValueError
