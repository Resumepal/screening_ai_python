# coding: utf-8

"""
    Screening AI API Docs

    API Documentation for Screening AI

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from screening_ai.models.create_platform_organisation_billing_stripe_session_response_dto import CreatePlatformOrganisationBillingStripeSessionResponseDto

class TestCreatePlatformOrganisationBillingStripeSessionResponseDto(unittest.TestCase):
    """CreatePlatformOrganisationBillingStripeSessionResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePlatformOrganisationBillingStripeSessionResponseDto:
        """Test CreatePlatformOrganisationBillingStripeSessionResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePlatformOrganisationBillingStripeSessionResponseDto`
        """
        model = CreatePlatformOrganisationBillingStripeSessionResponseDto()
        if include_optional:
            return CreatePlatformOrganisationBillingStripeSessionResponseDto(
                message = '',
                stripe_payment_session_id = ''
            )
        else:
            return CreatePlatformOrganisationBillingStripeSessionResponseDto(
                message = '',
                stripe_payment_session_id = '',
        )
        """

    def testCreatePlatformOrganisationBillingStripeSessionResponseDto(self):
        """Test CreatePlatformOrganisationBillingStripeSessionResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
