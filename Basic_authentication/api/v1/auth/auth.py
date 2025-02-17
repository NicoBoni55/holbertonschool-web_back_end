#!/usr/bin/env python3
"""Authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Class to manage auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header
        """
        if request is None:
            return None
        else:
            return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        return None
