# GetOrganisationMemberStatusResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organisation ID | 
**org_alias** | **str** | Organisation Alias | 
**platform_user_id** | **str** | Platform User ID | 
**email** | **str** | Email of the user | 
**first_name** | **str** | First name of the user | 
**last_name** | **str** | Last name of the user | 
**dp_url** | **str** | Profile Picture URL of the user | 
**status** | **str** | Status of the user | 
**created_at** | **str** | Time of user creation in ISO Date Time String Format | 

## Example

```python
from screening_ai.models.get_organisation_member_status_response_dto import GetOrganisationMemberStatusResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganisationMemberStatusResponseDto from a JSON string
get_organisation_member_status_response_dto_instance = GetOrganisationMemberStatusResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetOrganisationMemberStatusResponseDto.to_json())

# convert the object into a dict
get_organisation_member_status_response_dto_dict = get_organisation_member_status_response_dto_instance.to_dict()
# create an instance of GetOrganisationMemberStatusResponseDto from a dict
get_organisation_member_status_response_dto_from_dict = GetOrganisationMemberStatusResponseDto.from_dict(get_organisation_member_status_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


