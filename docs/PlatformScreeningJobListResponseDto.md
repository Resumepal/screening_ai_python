# PlatformScreeningJobListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_jobs** | [**List[PlatformScreeningJobResponseDto]**](PlatformScreeningJobResponseDto.md) | List of Screening Jobs | 

## Example

```python
from screening_ai.models.platform_screening_job_list_response_dto import PlatformScreeningJobListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformScreeningJobListResponseDto from a JSON string
platform_screening_job_list_response_dto_instance = PlatformScreeningJobListResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformScreeningJobListResponseDto.to_json())

# convert the object into a dict
platform_screening_job_list_response_dto_dict = platform_screening_job_list_response_dto_instance.to_dict()
# create an instance of PlatformScreeningJobListResponseDto from a dict
platform_screening_job_list_response_dto_from_dict = PlatformScreeningJobListResponseDto.from_dict(platform_screening_job_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


