#!/usr/bin/env python3
"""Definition of class TestAccessNestedMap"""
import unittest
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map


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
