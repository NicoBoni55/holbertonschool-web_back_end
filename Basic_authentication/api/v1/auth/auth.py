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
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += "/"
        for element in excluded_paths:
            if element.endswith('*'):
                if path.startswith(element[:1]):
                    return False
        if path in excluded_paths:
            return False
        else:
            return True

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
