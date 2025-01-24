# coding: utf-8

"""
    Screening AI API Docs

    API Documentation for Screening AI

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from screening_ai.models.platform_screening_submission_list_response_dto import PlatformScreeningSubmissionListResponseDto

class TestPlatformScreeningSubmissionListResponseDto(unittest.TestCase):
    """PlatformScreeningSubmissionListResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlatformScreeningSubmissionListResponseDto:
        """Test PlatformScreeningSubmissionListResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlatformScreeningSubmissionListResponseDto`
        """
        model = PlatformScreeningSubmissionListResponseDto()
        if include_optional:
            return PlatformScreeningSubmissionListResponseDto(
                screening_submissions = [
                    screening_ai.models.platform_screening_submission_response_dto.PlatformScreeningSubmissionResponseDto(
                        screening_submission_id = '', 
                        org_id = '', 
                        org_alias = '', 
                        email = '', 
                        first_name = '', 
                        last_name = '', 
                        phone_number = '', 
                        screening_job_id = '', 
                        chat = [
                            screening_ai.models.screening_form_submission_question_dto.ScreeningFormSubmissionQuestionDto(
                                index = 1.337, 
                                agent = '', 
                                human = '', 
                                human_audio_url = '', 
                                answer_type = '', 
                                answers_given = [
                                    ''
                                    ], )
                            ], 
                        created_at = '', 
                        status = '', 
                        upvotes = [
                            ''
                            ], 
                        is_viewed = True, 
                        is_private = True, )
                    ]
            )
        else:
            return PlatformScreeningSubmissionListResponseDto(
                screening_submissions = [
                    screening_ai.models.platform_screening_submission_response_dto.PlatformScreeningSubmissionResponseDto(
                        screening_submission_id = '', 
                        org_id = '', 
                        org_alias = '', 
                        email = '', 
                        first_name = '', 
                        last_name = '', 
                        phone_number = '', 
                        screening_job_id = '', 
                        chat = [
                            screening_ai.models.screening_form_submission_question_dto.ScreeningFormSubmissionQuestionDto(
                                index = 1.337, 
                                agent = '', 
                                human = '', 
                                human_audio_url = '', 
                                answer_type = '', 
                                answers_given = [
                                    ''
                                    ], )
                            ], 
                        created_at = '', 
                        status = '', 
                        upvotes = [
                            ''
                            ], 
                        is_viewed = True, 
                        is_private = True, )
                    ],
        )
        """

    def testPlatformScreeningSubmissionListResponseDto(self):
        """Test PlatformScreeningSubmissionListResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
