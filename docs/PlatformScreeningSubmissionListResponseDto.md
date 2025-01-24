# PlatformScreeningSubmissionListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_submissions** | [**List[PlatformScreeningSubmissionResponseDto]**](PlatformScreeningSubmissionResponseDto.md) | Screening Submissions | 

## Example

```python
from screening_ai.models.platform_screening_submission_list_response_dto import PlatformScreeningSubmissionListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformScreeningSubmissionListResponseDto from a JSON string
platform_screening_submission_list_response_dto_instance = PlatformScreeningSubmissionListResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformScreeningSubmissionListResponseDto.to_json())

# convert the object into a dict
platform_screening_submission_list_response_dto_dict = platform_screening_submission_list_response_dto_instance.to_dict()
# create an instance of PlatformScreeningSubmissionListResponseDto from a dict
platform_screening_submission_list_response_dto_from_dict = PlatformScreeningSubmissionListResponseDto.from_dict(platform_screening_submission_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


