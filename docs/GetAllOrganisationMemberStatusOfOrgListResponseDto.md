# GetAllOrganisationMemberStatusOfOrgListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_members** | **List[str]** | Accpeted Members Object List | 
**sent_members** | **List[str]** | Sent Members Object List | 
**super_admin** | **object** | Super Admin | 

## Example

```python
from screening_ai.models.get_all_organisation_member_status_of_org_list_response_dto import GetAllOrganisationMemberStatusOfOrgListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllOrganisationMemberStatusOfOrgListResponseDto from a JSON string
get_all_organisation_member_status_of_org_list_response_dto_instance = GetAllOrganisationMemberStatusOfOrgListResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetAllOrganisationMemberStatusOfOrgListResponseDto.to_json())

# convert the object into a dict
get_all_organisation_member_status_of_org_list_response_dto_dict = get_all_organisation_member_status_of_org_list_response_dto_instance.to_dict()
# create an instance of GetAllOrganisationMemberStatusOfOrgListResponseDto from a dict
get_all_organisation_member_status_of_org_list_response_dto_from_dict = GetAllOrganisationMemberStatusOfOrgListResponseDto.from_dict(get_all_organisation_member_status_of_org_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


