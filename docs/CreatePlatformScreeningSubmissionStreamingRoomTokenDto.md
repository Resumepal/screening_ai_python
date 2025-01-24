# CreatePlatformScreeningSubmissionStreamingRoomTokenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_job_id** | **str** | Screening Job ID | 
**screening_submission_id** | **str** | Screening Submission ID | 
**curr_date_time_epoch** | **float** | Current Date Time in Epoch | 

## Example

```python
from screening_ai.models.create_platform_screening_submission_streaming_room_token_dto import CreatePlatformScreeningSubmissionStreamingRoomTokenDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlatformScreeningSubmissionStreamingRoomTokenDto from a JSON string
create_platform_screening_submission_streaming_room_token_dto_instance = CreatePlatformScreeningSubmissionStreamingRoomTokenDto.from_json(json)
# print the JSON string representation of the object
print(CreatePlatformScreeningSubmissionStreamingRoomTokenDto.to_json())

# convert the object into a dict
create_platform_screening_submission_streaming_room_token_dto_dict = create_platform_screening_submission_streaming_room_token_dto_instance.to_dict()
# create an instance of CreatePlatformScreeningSubmissionStreamingRoomTokenDto from a dict
create_platform_screening_submission_streaming_room_token_dto_from_dict = CreatePlatformScreeningSubmissionStreamingRoomTokenDto.from_dict(create_platform_screening_submission_streaming_room_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


