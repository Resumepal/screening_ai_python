# ScreeningFormSubmissionQuestionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** | Index of the question | 
**agent** | **str** | Agent Question | 
**human** | **str** | Human Answer | 
**human_audio_url** | **str** | Human Answer Audio URL | 
**answer_type** | **str** | Answer Type | 
**answers_given** | **List[str]** | Answers Given | 

## Example

```python
from screening_ai.models.screening_form_submission_question_dto import ScreeningFormSubmissionQuestionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningFormSubmissionQuestionDto from a JSON string
screening_form_submission_question_dto_instance = ScreeningFormSubmissionQuestionDto.from_json(json)
# print the JSON string representation of the object
print(ScreeningFormSubmissionQuestionDto.to_json())

# convert the object into a dict
screening_form_submission_question_dto_dict = screening_form_submission_question_dto_instance.to_dict()
# create an instance of ScreeningFormSubmissionQuestionDto from a dict
screening_form_submission_question_dto_from_dict = ScreeningFormSubmissionQuestionDto.from_dict(screening_form_submission_question_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


