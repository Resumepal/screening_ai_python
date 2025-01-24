# UpdatePlatformScreeningSubmissionsStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_submission_ids** | **List[str]** | Screening Submission IDs | 
**status** | **str** | Submission Status | 

## Example

```python
from screening_ai.models.update_platform_screening_submissions_status_dto import UpdatePlatformScreeningSubmissionsStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlatformScreeningSubmissionsStatusDto from a JSON string
update_platform_screening_submissions_status_dto_instance = UpdatePlatformScreeningSubmissionsStatusDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePlatformScreeningSubmissionsStatusDto.to_json())

# convert the object into a dict
update_platform_screening_submissions_status_dto_dict = update_platform_screening_submissions_status_dto_instance.to_dict()
# create an instance of UpdatePlatformScreeningSubmissionsStatusDto from a dict
update_platform_screening_submissions_status_dto_from_dict = UpdatePlatformScreeningSubmissionsStatusDto.from_dict(update_platform_screening_submissions_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


