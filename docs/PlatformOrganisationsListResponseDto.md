# PlatformOrganisationsListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organisations** | **List[str]** | List of Organisations | 

## Example

```python
from screening_ai.models.platform_organisations_list_response_dto import PlatformOrganisationsListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformOrganisationsListResponseDto from a JSON string
platform_organisations_list_response_dto_instance = PlatformOrganisationsListResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformOrganisationsListResponseDto.to_json())

# convert the object into a dict
platform_organisations_list_response_dto_dict = platform_organisations_list_response_dto_instance.to_dict()
# create an instance of PlatformOrganisationsListResponseDto from a dict
platform_organisations_list_response_dto_from_dict = PlatformOrganisationsListResponseDto.from_dict(platform_organisations_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


