#!/usr/bin/env python3
""" Auth
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """ hash password
    """
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    return hash
