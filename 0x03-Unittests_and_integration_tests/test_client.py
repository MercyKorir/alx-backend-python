#!/usr/bin/env python3
"""Definition of a class TestGithubOrgClient"""
import unittest
from unittest import mock
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Any


class TestGithubOrgClient(unittest.TestCase):
    """Inherits from TestCase"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, name: str, mock_get_json: Any) -> None:
        """test the GithubOrgClient.org"""
        test_val = {
            'name': name,
            'description': '{} is a test organization'.format(name),
            'repos_url': 'https://api.github.com/orgs/{}/repos'.format(name)
        }
        mock_get_json.return_value = test_val
        client = GithubOrgClient(name)
        res = client.org
        self.assertEqual(res, test_val)
        link = 'https://api.github.com/orgs/'
        mock_get_json.assert_called_once_with('{}{}'.format(link, name))

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: PropertyMock) -> None:
        """Test for _public_repos_url property"""

        payload = {
            'name': 'google',
            'repos_url': 'https://api.github.com/orgs/google/repos',
        }
        mock_org.return_value = payload
        client = GithubOrgClient('google')
        self.assertEqual(client._public_repos_url, payload['repos_url'])
        mock_org.assert_called_once_with()
