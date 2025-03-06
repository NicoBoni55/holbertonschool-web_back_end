#!/usr/bin/env python3
"""
unittest
"""

from unittest import TestCase, mock
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ unittest access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ check acess_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ check exception
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertRaises(expected, e.exception)


class TestGetJson(TestCase):
    """
    class to http
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test get json
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """ class to memorization
    """

    def test_memorize(self):
        """ test memorize
        """
        class TestClass:
            """ test class
            """
            def a_method(self):
                """
                method a
                """
                return 42

            @memoize
            def a_property(self):
                """ property
                """
                return self.a_method()

        with patch.object(TestClass, "a_method") as method:
            test_class = TestClass
            test_class.a_property
            test_class.a_property
            method.assert_called_once
