# ApiResponseWrapperData

Actual response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Token | 
**url** | **str** | Url | 
**data** | **str** | Text from Audio | 
**answer_location** | **str** | Audio Url | 
**screening_submission_id** | **str** | Screening Submission Id | 
**org_id** | **str** | Organisation ID | 
**org_alias** | **str** | Organisation Alias | 
**email** | **str** | Email of the user | 
**first_name** | **str** | First name of the user | 
**last_name** | **str** | Last name of the user | 
**phone_number** | **str** | Phone Number | 
**screening_job_id** | **str** | Screening Job Id | 
**chat** | [**List[ScreeningFormSubmissionQuestionDto]**](ScreeningFormSubmissionQuestionDto.md) | Chat | 
**created_at** | **str** | Time of user creation in ISO Date Time String Format | 
**status** | **str** | Status of the user | 
**upvotes** | **List[str]** | Upvoted By | 
**is_viewed** | **bool** | Is Viewed | 
**is_private** | **bool** | Is Private | 
**screening_submissions** | [**List[PlatformScreeningSubmissionResponseDto]**](PlatformScreeningSubmissionResponseDto.md) | Screening Submissions | 
**screening_templates** | [**List[CreateScreeningTemplateDto]**](CreateScreeningTemplateDto.md) | Screening Templates | 
**screening_template_id** | **str** | Screening Template ID | 
**title** | **str** | Screening Job Title | 
**job_active** | **bool** | Screening Job Active Status | 
**jd** | **str** | Screening Job JD | 
**screening_jobs** | [**List[PlatformScreeningJobResponseDto]**](PlatformScreeningJobResponseDto.md) | List of Screening Jobs | 
**platform_user_id** | **str** | Platform User ID | 
**dp_url** | **str** | Profile Picture URL of the user | 
**jwt** | **str** | JWT Token | 
**org_name** | **str** | Organisation name | 
**org_dp_url** | **str** | Organisation Dp Url | 
**org_super_admin** | **str** | Organisation Super Admin Id | 
**org_admins** | **List[str]** | Organisation Admins | 
**org_joined_at** | **str** | Organisation Joining Date | 
**org_country** | **str** | Organisation Country | 
**org_city** | **str** | Organisation City | 
**org_state** | **str** | Organisation State | 
**org_active** | **bool** | Organisation Active Status | 
**updated_at** | **str** | Last Updated date in ISO Date Time String | 
**organisations** | **List[str]** | List of Organisations | 
**api_key** | **str** | Api Key | 
**organisation_alias** | **str** | Organisation Alias | 
**organisation_id** | **str** | Organisation Id | 
**org_super_admin_id** | **str** | Organisation Super Admin ID | 
**balance** | **float** | Balance | 
**currency** | **str** | Currency | 
**usage** | **List[str]** | Usage | 
**transactions** | **List[str]** | Transactions | 
**last_updated** | **str** | Last Updated | 
**message** | **str** | Message | 
**stripe_payment_session_id** | **str** | Stripe Payment Session ID | 
**accepted_members** | **List[str]** | Accpeted Members Object List | 
**sent_members** | **List[str]** | Sent Members Object List | 
**super_admin** | **object** | Super Admin | 

## Example

```python
from screening_ai.models.api_response_wrapper_data import ApiResponseWrapperData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseWrapperData from a JSON string
api_response_wrapper_data_instance = ApiResponseWrapperData.from_json(json)
# print the JSON string representation of the object
print(ApiResponseWrapperData.to_json())

# convert the object into a dict
api_response_wrapper_data_dict = api_response_wrapper_data_instance.to_dict()
# create an instance of ApiResponseWrapperData from a dict
api_response_wrapper_data_from_dict = ApiResponseWrapperData.from_dict(api_response_wrapper_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


