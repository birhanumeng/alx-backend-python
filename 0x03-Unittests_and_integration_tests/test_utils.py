#!/usr/bin/env python3
""" Unittest and integrated test module """

from unittest import TestCase, mock
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Parameterize a unit test class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, output):
        """ Test the parametrized input with its output """
        self.assertEqual(access_nested_map(map, path), output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test that it raises KeyError with some inputs """
        with self.assertRaises(KeyError) as err:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, err.exception)


class TestGetJson(TestCase):
    """ Json response method test class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test the mocked get method was called with test_url as argument """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """ Testing memoization """

    def test_memoize(self):
        """ Memoization function """

        class TestClass:
            """ Testing class """

            def a_method(self):
                """ It returns 42 always """
                return 42

            @memoize
            def a_property(self):
                """ Memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
