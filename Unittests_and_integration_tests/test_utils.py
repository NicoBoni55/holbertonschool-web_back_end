#!/usr/bin/env python3
"""
unittest
"""

import unittest

from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ unittest access_nested_map
    """

    @parameterized.expand([
        {"a": 1}, ("a"),
        {"a": {"b": 2}}, ("a",),
        {"a": {"b": 2}}, ("a", "b")
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ check acess_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
