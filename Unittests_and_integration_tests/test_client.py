#!/usr/bin/env python3
"""
Test Client
"""

from unittest import TestCase
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock


class TestGithubOrgClient(TestCase):
    """
    Test Github
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """ test org
        """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once
