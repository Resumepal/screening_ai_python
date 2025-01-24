# PlatformUserResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_user_id** | **str** | Platform User ID | 
**email** | **str** | Email of the user | 
**created_at** | **str** | Time of user creation in ISO Date Time String Format | 
**first_name** | **str** | First name of the user | 
**last_name** | **str** | Last name of the user | 
**dp_url** | **str** | Profile Picture URL of the user | 

## Example

```python
from screening_ai.models.platform_user_response_dto import PlatformUserResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformUserResponseDto from a JSON string
platform_user_response_dto_instance = PlatformUserResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformUserResponseDto.to_json())

# convert the object into a dict
platform_user_response_dto_dict = platform_user_response_dto_instance.to_dict()
# create an instance of PlatformUserResponseDto from a dict
platform_user_response_dto_from_dict = PlatformUserResponseDto.from_dict(platform_user_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


