# ApiResponseWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **float** | HTTP status code | 
**description** | **str** | Description of the response | 
**data** | [**ApiResponseWrapperData**](ApiResponseWrapperData.md) |  | 

## Example

```python
from screening_ai.models.api_response_wrapper import ApiResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponseWrapper from a JSON string
api_response_wrapper_instance = ApiResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(ApiResponseWrapper.to_json())

# convert the object into a dict
api_response_wrapper_dict = api_response_wrapper_instance.to_dict()
# create an instance of ApiResponseWrapper from a dict
api_response_wrapper_from_dict = ApiResponseWrapper.from_dict(api_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


