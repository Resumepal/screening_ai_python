# coding: utf-8

"""
    Screening AI API Docs

    API Documentation for Screening AI

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from screening_ai.models.get_platform_organisation_api_key_response_dto import GetPlatformOrganisationApiKeyResponseDto

class TestGetPlatformOrganisationApiKeyResponseDto(unittest.TestCase):
    """GetPlatformOrganisationApiKeyResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPlatformOrganisationApiKeyResponseDto:
        """Test GetPlatformOrganisationApiKeyResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPlatformOrganisationApiKeyResponseDto`
        """
        model = GetPlatformOrganisationApiKeyResponseDto()
        if include_optional:
            return GetPlatformOrganisationApiKeyResponseDto(
                api_key = '',
                organisation_alias = '',
                organisation_id = ''
            )
        else:
            return GetPlatformOrganisationApiKeyResponseDto(
                api_key = '',
                organisation_alias = '',
                organisation_id = '',
        )
        """

    def testGetPlatformOrganisationApiKeyResponseDto(self):
        """Test GetPlatformOrganisationApiKeyResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
