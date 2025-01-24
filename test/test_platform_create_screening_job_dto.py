# coding: utf-8

"""
    Screening AI API Docs

    API Documentation for Screening AI

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from screening_ai.models.platform_create_screening_job_dto import PlatformCreateScreeningJobDto

class TestPlatformCreateScreeningJobDto(unittest.TestCase):
    """PlatformCreateScreeningJobDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlatformCreateScreeningJobDto:
        """Test PlatformCreateScreeningJobDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlatformCreateScreeningJobDto`
        """
        model = PlatformCreateScreeningJobDto()
        if include_optional:
            return PlatformCreateScreeningJobDto(
                screening_template_id = '',
                title = '',
                job_active = True,
                jd = '',
                upvotes = [
                    ''
                    ],
                created_at = ''
            )
        else:
            return PlatformCreateScreeningJobDto(
                screening_template_id = '',
                title = '',
                job_active = True,
                jd = '',
                upvotes = [
                    ''
                    ],
                created_at = '',
        )
        """

    def testPlatformCreateScreeningJobDto(self):
        """Test PlatformCreateScreeningJobDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
