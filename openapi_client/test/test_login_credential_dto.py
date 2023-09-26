# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.login_credential_dto import LoginCredentialDto  # noqa: E501

class TestLoginCredentialDto(unittest.TestCase):
    """LoginCredentialDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoginCredentialDto:
        """Test LoginCredentialDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoginCredentialDto`
        """
        model = LoginCredentialDto()  # noqa: E501
        if include_optional:
            return LoginCredentialDto(
                email = 'testuser@email.com',
                password = 'password'
            )
        else:
            return LoginCredentialDto(
                email = 'testuser@email.com',
                password = 'password',
        )
        """

    def testLoginCredentialDto(self):
        """Test LoginCredentialDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()