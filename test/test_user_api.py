# coding: utf-8

"""
    Squac API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.user_api import UserApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_create_create(self):
        """Test case for user_create_create

        """
        pass

    def test_user_me_partial_update(self):
        """Test case for user_me_partial_update

        """
        pass

    def test_user_me_read(self):
        """Test case for user_me_read

        """
        pass

    def test_user_me_update(self):
        """Test case for user_me_update

        """
        pass

    def test_user_token_create(self):
        """Test case for user_token_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
