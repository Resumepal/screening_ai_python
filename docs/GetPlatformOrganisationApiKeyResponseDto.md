# GetPlatformOrganisationApiKeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Api Key | 
**organisation_alias** | **str** | Organisation Alias | 
**organisation_id** | **str** | Organisation Id | 

## Example

```python
from screening_ai.models.get_platform_organisation_api_key_response_dto import GetPlatformOrganisationApiKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlatformOrganisationApiKeyResponseDto from a JSON string
get_platform_organisation_api_key_response_dto_instance = GetPlatformOrganisationApiKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetPlatformOrganisationApiKeyResponseDto.to_json())

# convert the object into a dict
get_platform_organisation_api_key_response_dto_dict = get_platform_organisation_api_key_response_dto_instance.to_dict()
# create an instance of GetPlatformOrganisationApiKeyResponseDto from a dict
get_platform_organisation_api_key_response_dto_from_dict = GetPlatformOrganisationApiKeyResponseDto.from_dict(get_platform_organisation_api_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


