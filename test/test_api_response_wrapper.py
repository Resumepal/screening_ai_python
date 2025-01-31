# coding: utf-8

"""
    Screening AI API Docs

    API Documentation for Screening AI

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from screening_ai.models.api_response_wrapper import ApiResponseWrapper

class TestApiResponseWrapper(unittest.TestCase):
    """ApiResponseWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResponseWrapper:
        """Test ApiResponseWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResponseWrapper`
        """
        model = ApiResponseWrapper()
        if include_optional:
            return ApiResponseWrapper(
                status = 200,
                description = 'Screening Submission Streaming Room Created',
                data = None
            )
        else:
            return ApiResponseWrapper(
                status = 200,
                description = 'Screening Submission Streaming Room Created',
                data = None,
        )
        """

    def testApiResponseWrapper(self):
        """Test ApiResponseWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
