# PlatformCreateScreeningJobDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_template_id** | **str** | Screening Template ID | 
**title** | **str** | Screening Job Title | 
**job_active** | **bool** | Screening Job Active Status | 
**jd** | **str** | Screening Job JD | 
**upvotes** | **List[str]** | Screening Job Upvotes | 
**created_at** | **str** | Creation date in ISO Date Time String | 

## Example

```python
from screening_ai.models.platform_create_screening_job_dto import PlatformCreateScreeningJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformCreateScreeningJobDto from a JSON string
platform_create_screening_job_dto_instance = PlatformCreateScreeningJobDto.from_json(json)
# print the JSON string representation of the object
print(PlatformCreateScreeningJobDto.to_json())

# convert the object into a dict
platform_create_screening_job_dto_dict = platform_create_screening_job_dto_instance.to_dict()
# create an instance of PlatformCreateScreeningJobDto from a dict
platform_create_screening_job_dto_from_dict = PlatformCreateScreeningJobDto.from_dict(platform_create_screening_job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


