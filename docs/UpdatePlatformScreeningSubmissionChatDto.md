# UpdatePlatformScreeningSubmissionChatDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_submission_id** | **str** | Screening Submission ID | 
**index** | **float** | Index of the question | 
**human** | **str** | Agent Question | 
**human_audio_url** | **str** | Human Answer | 
**answer_type** | **str** | Answer Type | 

## Example

```python
from screening_ai.models.update_platform_screening_submission_chat_dto import UpdatePlatformScreeningSubmissionChatDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlatformScreeningSubmissionChatDto from a JSON string
update_platform_screening_submission_chat_dto_instance = UpdatePlatformScreeningSubmissionChatDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePlatformScreeningSubmissionChatDto.to_json())

# convert the object into a dict
update_platform_screening_submission_chat_dto_dict = update_platform_screening_submission_chat_dto_instance.to_dict()
# create an instance of UpdatePlatformScreeningSubmissionChatDto from a dict
update_platform_screening_submission_chat_dto_from_dict = UpdatePlatformScreeningSubmissionChatDto.from_dict(update_platform_screening_submission_chat_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


