# PlatformScreeningSubmissionTextFromAudioResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Text from Audio | 
**answer_location** | **str** | Audio Url | 

## Example

```python
from screening_ai.models.platform_screening_submission_text_from_audio_response_dto import PlatformScreeningSubmissionTextFromAudioResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformScreeningSubmissionTextFromAudioResponseDto from a JSON string
platform_screening_submission_text_from_audio_response_dto_instance = PlatformScreeningSubmissionTextFromAudioResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformScreeningSubmissionTextFromAudioResponseDto.to_json())

# convert the object into a dict
platform_screening_submission_text_from_audio_response_dto_dict = platform_screening_submission_text_from_audio_response_dto_instance.to_dict()
# create an instance of PlatformScreeningSubmissionTextFromAudioResponseDto from a dict
platform_screening_submission_text_from_audio_response_dto_from_dict = PlatformScreeningSubmissionTextFromAudioResponseDto.from_dict(platform_screening_submission_text_from_audio_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


