# PlatformScreeningSubmissionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_submission_id** | **str** | Screening Submission ID | 
**org_id** | **str** | Organisation ID | 
**org_alias** | **str** | Organisation Alias | 
**email** | **str** | Email | 
**first_name** | **str** | First Name | 
**last_name** | **str** | Last Name | 
**phone_number** | **str** | Phone Number | 
**screening_job_id** | **str** | Screening Job ID | 
**chat** | [**List[ScreeningFormSubmissionQuestionDto]**](ScreeningFormSubmissionQuestionDto.md) | Chat | 
**created_at** | **str** | Created At | 
**status** | **str** | Status | 
**upvotes** | **List[str]** | Upvotes | 
**is_viewed** | **bool** | Is Viewed | 
**is_private** | **bool** | Is Private | 

## Example

```python
from screening_ai.models.platform_screening_submission_response_dto import PlatformScreeningSubmissionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformScreeningSubmissionResponseDto from a JSON string
platform_screening_submission_response_dto_instance = PlatformScreeningSubmissionResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformScreeningSubmissionResponseDto.to_json())

# convert the object into a dict
platform_screening_submission_response_dto_dict = platform_screening_submission_response_dto_instance.to_dict()
# create an instance of PlatformScreeningSubmissionResponseDto from a dict
platform_screening_submission_response_dto_from_dict = PlatformScreeningSubmissionResponseDto.from_dict(platform_screening_submission_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


