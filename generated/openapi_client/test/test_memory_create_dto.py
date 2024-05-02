# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.103.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.memory_create_dto import MemoryCreateDto

class TestMemoryCreateDto(unittest.TestCase):
    """MemoryCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemoryCreateDto:
        """Test MemoryCreateDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemoryCreateDto`
        """
        model = MemoryCreateDto()
        if include_optional:
            return MemoryCreateDto(
                asset_ids = [
                    ''
                    ],
                data = openapi_client.models.on_this_day_dto.OnThisDayDto(
                    year = 1, ),
                is_saved = True,
                memory_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                seen_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = 'on_this_day'
            )
        else:
            return MemoryCreateDto(
                data = openapi_client.models.on_this_day_dto.OnThisDayDto(
                    year = 1, ),
                memory_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = 'on_this_day',
        )
        """

    def testMemoryCreateDto(self):
        """Test MemoryCreateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
