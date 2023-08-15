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
