#!/usr/bin/env python3
"""
function filter_datum - that return the log message
"""

import re


def filter_datum(fields, message):
    
    x = re.search(fields, message)

    if x:
        print(f"Encontre:{x.group()}")
    else:
        print("No encontre nada")


