#!/usr/bin/env python3
"""
function filter_datum - that return the log message
"""

import re
from typing import List


import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filter values with filter_datum
        """
        message = filter_datum(self.fields, self.REDACTION,
                               super().format(record), self.SEPARATOR)

        return message


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ returns the log message obfuscated
    """
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator, message)

    return message
