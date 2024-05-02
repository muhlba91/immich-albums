# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.103.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.validate_library_import_path_response_dto import ValidateLibraryImportPathResponseDto

class TestValidateLibraryImportPathResponseDto(unittest.TestCase):
    """ValidateLibraryImportPathResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateLibraryImportPathResponseDto:
        """Test ValidateLibraryImportPathResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateLibraryImportPathResponseDto`
        """
        model = ValidateLibraryImportPathResponseDto()
        if include_optional:
            return ValidateLibraryImportPathResponseDto(
                import_path = '',
                is_valid = True,
                message = ''
            )
        else:
            return ValidateLibraryImportPathResponseDto(
                import_path = '',
                is_valid = True,
        )
        """

    def testValidateLibraryImportPathResponseDto(self):
        """Test ValidateLibraryImportPathResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()