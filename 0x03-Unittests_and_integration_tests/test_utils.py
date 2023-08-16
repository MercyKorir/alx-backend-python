#!/usr/bin/env python3
"""Definition of class TestAccessNestedMap"""
import unittest
import unittest.mock
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
    def test_get_json(self, mock_get):
        """Test for get_json"""

        vals = [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
        for test_url, test_payload in vals:
            with self.subTest(test_url=test_url, test_payload=test_payload):
                mock_res = unittest.mock.Mock()
                mock_res.json.return_value = test_payload
                mock_get.return_value = mock_res
                res = get_json(test_url)
                self.assertEqual(res, test_payload)
                mock_get.assert_called_once_with(test_url)
                mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """Inherits from TestCase"""

    def test_memoize(self) -> None:
        """Contains definition of a class"""

        class TestClass:
            """Contains two methods"""

            def a_method(self) -> int:
                """Returns 42"""
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        obj = TestClass()

        with unittest.mock.patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            res1 = obj.a_property
            res2 = obj.a_property
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
            mock_method.assert_called_once()
