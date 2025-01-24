# GetPlatformScreeningSubmissionsOfOrgDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_alias** | **str** | Organisation Alias | 
**job_id** | **str** | Job ID | 
**status** | **str** | Submission Status | 
**start_after** | **str** | Start After | 
**limit** | **float** | Limit | 

## Example

```python
from screening_ai.models.get_platform_screening_submissions_of_org_dto import GetPlatformScreeningSubmissionsOfOrgDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlatformScreeningSubmissionsOfOrgDto from a JSON string
get_platform_screening_submissions_of_org_dto_instance = GetPlatformScreeningSubmissionsOfOrgDto.from_json(json)
# print the JSON string representation of the object
print(GetPlatformScreeningSubmissionsOfOrgDto.to_json())

# convert the object into a dict
get_platform_screening_submissions_of_org_dto_dict = get_platform_screening_submissions_of_org_dto_instance.to_dict()
# create an instance of GetPlatformScreeningSubmissionsOfOrgDto from a dict
get_platform_screening_submissions_of_org_dto_from_dict = GetPlatformScreeningSubmissionsOfOrgDto.from_dict(get_platform_screening_submissions_of_org_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


