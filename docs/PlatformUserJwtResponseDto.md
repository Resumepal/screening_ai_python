# PlatformUserJwtResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | JWT Token | 

## Example

```python
from screening_ai.models.platform_user_jwt_response_dto import PlatformUserJwtResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformUserJwtResponseDto from a JSON string
platform_user_jwt_response_dto_instance = PlatformUserJwtResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlatformUserJwtResponseDto.to_json())

# convert the object into a dict
platform_user_jwt_response_dto_dict = platform_user_jwt_response_dto_instance.to_dict()
# create an instance of PlatformUserJwtResponseDto from a dict
platform_user_jwt_response_dto_from_dict = PlatformUserJwtResponseDto.from_dict(platform_user_jwt_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


