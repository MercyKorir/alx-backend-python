#!/usr/bin/env python3
"""Definition of class TestAccessNestedMap"""
import unittest
import unittest.mock
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Inherits from TestCase"""

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict[Any, Any],
                               path: Tuple[Any, ...], expected_output: Any):
        """tests access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b')),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[Any, Any],
                                         path: Tuple[Any, ...]):
        """tests for exception handling"""
        with self.assertRaises(KeyError) as ex:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ex.exception),
                         "'{}'".format(path[-1]))


class TestGetJson(unittest.TestCase):
    """Inherits from TestCase"""

    @unittest.mock.patch('requests.get')
    def test_get_json(self, mock_get: unittest.mock.Mock) -> None:
        """Test for get_json"""

        test_cases = [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
        for test_url, test_payload in test_cases:
            mock_get.return_value.json.return_value = test_payload
            res = get_json(test_url)
            mock_get.assert_called_with(test_url)
            self.assertEqual(res, test_payload)
