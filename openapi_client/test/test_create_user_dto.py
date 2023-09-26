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

from openapi_client.models.create_user_dto import CreateUserDto  # noqa: E501

class TestCreateUserDto(unittest.TestCase):
    """CreateUserDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUserDto:
        """Test CreateUserDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUserDto`
        """
        model = CreateUserDto()  # noqa: E501
        if include_optional:
            return CreateUserDto(
                email = '',
                external_path = '',
                first_name = '',
                last_name = '',
                memories_enabled = True,
                password = '',
                storage_label = ''
            )
        else:
            return CreateUserDto(
                email = '',
                first_name = '',
                last_name = '',
                password = '',
        )
        """

    def testCreateUserDto(self):
        """Test CreateUserDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()