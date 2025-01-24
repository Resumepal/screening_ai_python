# CreatePlatformOrganisationBillingStripeSessionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message | 
**stripe_payment_session_id** | **str** | Stripe Payment Session ID | 

## Example

```python
from screening_ai.models.create_platform_organisation_billing_stripe_session_response_dto import CreatePlatformOrganisationBillingStripeSessionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlatformOrganisationBillingStripeSessionResponseDto from a JSON string
create_platform_organisation_billing_stripe_session_response_dto_instance = CreatePlatformOrganisationBillingStripeSessionResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreatePlatformOrganisationBillingStripeSessionResponseDto.to_json())

# convert the object into a dict
create_platform_organisation_billing_stripe_session_response_dto_dict = create_platform_organisation_billing_stripe_session_response_dto_instance.to_dict()
# create an instance of CreatePlatformOrganisationBillingStripeSessionResponseDto from a dict
create_platform_organisation_billing_stripe_session_response_dto_from_dict = CreatePlatformOrganisationBillingStripeSessionResponseDto.from_dict(create_platform_organisation_billing_stripe_session_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


