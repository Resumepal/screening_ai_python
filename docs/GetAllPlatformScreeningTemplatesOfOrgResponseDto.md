# GetAllPlatformScreeningTemplatesOfOrgResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_templates** | [**List[CreateScreeningTemplateDto]**](CreateScreeningTemplateDto.md) | Screening Templates | 

## Example

```python
from screening_ai.models.get_all_platform_screening_templates_of_org_response_dto import GetAllPlatformScreeningTemplatesOfOrgResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPlatformScreeningTemplatesOfOrgResponseDto from a JSON string
get_all_platform_screening_templates_of_org_response_dto_instance = GetAllPlatformScreeningTemplatesOfOrgResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetAllPlatformScreeningTemplatesOfOrgResponseDto.to_json())

# convert the object into a dict
get_all_platform_screening_templates_of_org_response_dto_dict = get_all_platform_screening_templates_of_org_response_dto_instance.to_dict()
# create an instance of GetAllPlatformScreeningTemplatesOfOrgResponseDto from a dict
get_all_platform_screening_templates_of_org_response_dto_from_dict = GetAllPlatformScreeningTemplatesOfOrgResponseDto.from_dict(get_all_platform_screening_templates_of_org_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


