#!/usr/bin/env python3
""" Basic Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        basic = authorization_header.split(' ')
        return basic[1]
