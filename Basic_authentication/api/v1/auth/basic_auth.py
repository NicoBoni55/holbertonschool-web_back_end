#!/usr/bin/env python3
""" Basic Auth
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode base64
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encode = base64_authorization_header.encode('utf-8')
            encode = base64.b64decode(encode)
            decode = encode.decode('utf-8')
            return decode
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ extract user credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        credential = decoded_base64_authorization_header.split(":")
        return credential[0], credential[1]
