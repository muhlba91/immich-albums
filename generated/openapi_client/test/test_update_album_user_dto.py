# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.103.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.update_album_user_dto import UpdateAlbumUserDto

class TestUpdateAlbumUserDto(unittest.TestCase):
    """UpdateAlbumUserDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateAlbumUserDto:
        """Test UpdateAlbumUserDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateAlbumUserDto`
        """
        model = UpdateAlbumUserDto()
        if include_optional:
            return UpdateAlbumUserDto(
                role = 'editor'
            )
        else:
            return UpdateAlbumUserDto(
                role = 'editor',
        )
        """

    def testUpdateAlbumUserDto(self):
        """Test UpdateAlbumUserDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
