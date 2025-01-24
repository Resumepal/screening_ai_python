# PlatformScreeningJobResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_job_id** | **str** | Screening Job Id | 
**org_id** | **str** | Organisation ID | 
**org_alias** | **str** | Organisation alias | 
**screening_template_id** | **str** | Screening Template ID | 
**title** | **str** | Screening Job Title | 
**job_active** | **bool** | Screening Job Active Status | 
**jd** | **str** | Screening Job JD | 
**upvotes** | **List[str]** | Upvoted By | 
**created_at** | **str** | Creation date in ISO Date Time String | 

## Example

```python
from screening_ai.models.platform_screening_job_response_dto import PlatformScreeningJobResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformScreeningJobResponseDto from a JSON string
platform_screening_job_response_dto_instance = PlatformScreeningJobResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformScreeningJobResponseDto.to_json())

# convert the object into a dict
platform_screening_job_response_dto_dict = platform_screening_job_response_dto_instance.to_dict()
# create an instance of PlatformScreeningJobResponseDto from a dict
platform_screening_job_response_dto_from_dict = PlatformScreeningJobResponseDto.from_dict(platform_screening_job_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


