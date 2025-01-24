# PlatformOrganisationResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organisation ID | 
**org_name** | **str** | Organisation name | 
**org_alias** | **str** | Organisation alias | 
**org_dp_url** | **str** | Organisation Dp Url | 
**org_super_admin** | **str** | Organisation Super Admin Id | 
**org_admins** | **List[str]** | Organisation Admins | 
**org_joined_at** | **str** | Organisation Joining Date | 
**org_country** | **str** | Organisation Country | 
**org_city** | **str** | Organisation City | 
**org_state** | **str** | Organisation State | 
**org_active** | **bool** | Organisation Active Status | 
**created_at** | **str** | Creation date in ISO Date Time String | 
**updated_at** | **str** | Last Updated date in ISO Date Time String | 

## Example

```python
from screening_ai.models.platform_organisation_response_dto import PlatformOrganisationResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformOrganisationResponseDto from a JSON string
platform_organisation_response_dto_instance = PlatformOrganisationResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformOrganisationResponseDto.to_json())

# convert the object into a dict
platform_organisation_response_dto_dict = platform_organisation_response_dto_instance.to_dict()
# create an instance of PlatformOrganisationResponseDto from a dict
platform_organisation_response_dto_from_dict = PlatformOrganisationResponseDto.from_dict(platform_organisation_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


