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

from openapi_client.models.queue_status_dto import QueueStatusDto  # noqa: E501

class TestQueueStatusDto(unittest.TestCase):
    """QueueStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueueStatusDto:
        """Test QueueStatusDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueueStatusDto`
        """
        model = QueueStatusDto()  # noqa: E501
        if include_optional:
            return QueueStatusDto(
                is_active = True,
                is_paused = True
            )
        else:
            return QueueStatusDto(
                is_active = True,
                is_paused = True,
        )
        """

    def testQueueStatusDto(self):
        """Test QueueStatusDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()