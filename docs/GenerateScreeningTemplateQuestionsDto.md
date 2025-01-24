# GenerateScreeningTemplateQuestionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_title** | **str** | Task Title | 

## Example

```python
from screening_ai.models.generate_screening_template_questions_dto import GenerateScreeningTemplateQuestionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateScreeningTemplateQuestionsDto from a JSON string
generate_screening_template_questions_dto_instance = GenerateScreeningTemplateQuestionsDto.from_json(json)
# print the JSON string representation of the object
print(GenerateScreeningTemplateQuestionsDto.to_json())

# convert the object into a dict
generate_screening_template_questions_dto_dict = generate_screening_template_questions_dto_instance.to_dict()
# create an instance of GenerateScreeningTemplateQuestionsDto from a dict
generate_screening_template_questions_dto_from_dict = GenerateScreeningTemplateQuestionsDto.from_dict(generate_screening_template_questions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


