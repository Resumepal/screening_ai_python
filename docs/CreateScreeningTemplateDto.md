# CreateScreeningTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Template Title | 
**description** | **str** | Template Description | 
**prompt** | **str** | Template Prompt | 
**is_streaming** | **bool** | Is the Template Streaming (Real Time) | 
**questions** | **List[str]** | Template Questions | 
**created_at** | **str** | Created At | 

## Example

```python
from screening_ai.models.create_screening_template_dto import CreateScreeningTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScreeningTemplateDto from a JSON string
create_screening_template_dto_instance = CreateScreeningTemplateDto.from_json(json)
# print the JSON string representation of the object
print(CreateScreeningTemplateDto.to_json())

# convert the object into a dict
create_screening_template_dto_dict = create_screening_template_dto_instance.to_dict()
# create an instance of CreateScreeningTemplateDto from a dict
create_screening_template_dto_from_dict = CreateScreeningTemplateDto.from_dict(create_screening_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


