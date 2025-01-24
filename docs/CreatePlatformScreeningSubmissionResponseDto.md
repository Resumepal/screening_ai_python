# CreatePlatformScreeningSubmissionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_submission_id** | **str** | Screening Submission Id | 

## Example

```python
from screening_ai.models.create_platform_screening_submission_response_dto import CreatePlatformScreeningSubmissionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlatformScreeningSubmissionResponseDto from a JSON string
create_platform_screening_submission_response_dto_instance = CreatePlatformScreeningSubmissionResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreatePlatformScreeningSubmissionResponseDto.to_json())

# convert the object into a dict
create_platform_screening_submission_response_dto_dict = create_platform_screening_submission_response_dto_instance.to_dict()
# create an instance of CreatePlatformScreeningSubmissionResponseDto from a dict
create_platform_screening_submission_response_dto_from_dict = CreatePlatformScreeningSubmissionResponseDto.from_dict(create_platform_screening_submission_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


