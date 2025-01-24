# CreatePlatformScreeningFormSubmissionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organisation ID | 
**org_alias** | **str** | Organisation Alias | 
**email** | **str** | Email | 
**first_name** | **str** | First Name | 
**last_name** | **str** | Last Name | 
**phone_number** | **str** | Phone Number | 
**screening_job_id** | **str** | Screening Job ID | 
**chat** | **List[str]** | Chat | 
**created_at** | **str** | Created At | 
**status** | **str** | Status | 
**upvotes** | **List[str]** | Upvotes | 
**is_viewed** | **bool** | Is Viewed | 
**is_private** | **bool** | Is Private | 

## Example

```python
from screening_ai.models.create_platform_screening_form_submission_dto import CreatePlatformScreeningFormSubmissionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlatformScreeningFormSubmissionDto from a JSON string
create_platform_screening_form_submission_dto_instance = CreatePlatformScreeningFormSubmissionDto.from_json(json)
# print the JSON string representation of the object
print(CreatePlatformScreeningFormSubmissionDto.to_json())

# convert the object into a dict
create_platform_screening_form_submission_dto_dict = create_platform_screening_form_submission_dto_instance.to_dict()
# create an instance of CreatePlatformScreeningFormSubmissionDto from a dict
create_platform_screening_form_submission_dto_from_dict = CreatePlatformScreeningFormSubmissionDto.from_dict(create_platform_screening_form_submission_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


