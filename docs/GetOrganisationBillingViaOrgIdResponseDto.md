# GetOrganisationBillingViaOrgIdResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organisation ID | 
**org_alias** | **str** | Organisation Alias | 
**org_super_admin_id** | **str** | Organisation Super Admin ID | 
**balance** | **float** | Balance | 
**currency** | **str** | Currency | 
**usage** | **List[str]** | Usage | 
**transactions** | **List[str]** | Transactions | 
**last_updated** | **str** | Last Updated | 

## Example

```python
from screening_ai.models.get_organisation_billing_via_org_id_response_dto import GetOrganisationBillingViaOrgIdResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganisationBillingViaOrgIdResponseDto from a JSON string
get_organisation_billing_via_org_id_response_dto_instance = GetOrganisationBillingViaOrgIdResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetOrganisationBillingViaOrgIdResponseDto.to_json())

# convert the object into a dict
get_organisation_billing_via_org_id_response_dto_dict = get_organisation_billing_via_org_id_response_dto_instance.to_dict()
# create an instance of GetOrganisationBillingViaOrgIdResponseDto from a dict
get_organisation_billing_via_org_id_response_dto_from_dict = GetOrganisationBillingViaOrgIdResponseDto.from_dict(get_organisation_billing_via_org_id_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


