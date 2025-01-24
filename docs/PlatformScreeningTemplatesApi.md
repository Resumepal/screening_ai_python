# screening_ai.PlatformScreeningTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_screening_templates_controller_create_screening_template**](PlatformScreeningTemplatesApi.md#platform_screening_templates_controller_create_screening_template) | **POST** /api/v2/platform/platform-screening-template | Create a new Screening Template
[**platform_screening_templates_controller_generate_screening_template_questions**](PlatformScreeningTemplatesApi.md#platform_screening_templates_controller_generate_screening_template_questions) | **POST** /api/v2/platform/platform-screening-template/generateQuestions | Generate Screening Template Questions
[**platform_screening_templates_controller_get_screening_templates**](PlatformScreeningTemplatesApi.md#platform_screening_templates_controller_get_screening_templates) | **GET** /api/v2/platform/platform-screening-template | Get all Screening Templates of Organisation


# **platform_screening_templates_controller_create_screening_template**
> ApiResponseWrapper platform_screening_templates_controller_create_screening_template(create_screening_template_dto)

Create a new Screening Template

### Example

* Api Key Authentication (X-API-KEY):

```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.models.create_screening_template_dto import CreateScreeningTemplateDto
from screening_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = screening_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-API-KEY
configuration.api_key['X-API-KEY'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Enter a context with an instance of the API client
with screening_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = screening_ai.PlatformScreeningTemplatesApi(api_client)
    create_screening_template_dto = screening_ai.CreateScreeningTemplateDto() # CreateScreeningTemplateDto | 

    try:
        # Create a new Screening Template
        api_response = api_instance.platform_screening_templates_controller_create_screening_template(create_screening_template_dto)
        print("The response of PlatformScreeningTemplatesApi->platform_screening_templates_controller_create_screening_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningTemplatesApi->platform_screening_templates_controller_create_screening_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_screening_template_dto** | [**CreateScreeningTemplateDto**](CreateScreeningTemplateDto.md)|  | 

### Return type

[**ApiResponseWrapper**](ApiResponseWrapper.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Screening Template Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_templates_controller_generate_screening_template_questions**
> ApiResponseWrapper platform_screening_templates_controller_generate_screening_template_questions(generate_screening_template_questions_dto)

Generate Screening Template Questions

### Example

* Api Key Authentication (X-API-KEY):

```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.models.generate_screening_template_questions_dto import GenerateScreeningTemplateQuestionsDto
from screening_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = screening_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-API-KEY
configuration.api_key['X-API-KEY'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Enter a context with an instance of the API client
with screening_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = screening_ai.PlatformScreeningTemplatesApi(api_client)
    generate_screening_template_questions_dto = screening_ai.GenerateScreeningTemplateQuestionsDto() # GenerateScreeningTemplateQuestionsDto | 

    try:
        # Generate Screening Template Questions
        api_response = api_instance.platform_screening_templates_controller_generate_screening_template_questions(generate_screening_template_questions_dto)
        print("The response of PlatformScreeningTemplatesApi->platform_screening_templates_controller_generate_screening_template_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningTemplatesApi->platform_screening_templates_controller_generate_screening_template_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_screening_template_questions_dto** | [**GenerateScreeningTemplateQuestionsDto**](GenerateScreeningTemplateQuestionsDto.md)|  | 

### Return type

[**ApiResponseWrapper**](ApiResponseWrapper.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Screening Template Questions Generated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_templates_controller_get_screening_templates**
> ApiResponseWrapper platform_screening_templates_controller_get_screening_templates()

Get all Screening Templates of Organisation

### Example

* Api Key Authentication (X-API-KEY):

```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = screening_ai.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-API-KEY
configuration.api_key['X-API-KEY'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Enter a context with an instance of the API client
with screening_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = screening_ai.PlatformScreeningTemplatesApi(api_client)

    try:
        # Get all Screening Templates of Organisation
        api_response = api_instance.platform_screening_templates_controller_get_screening_templates()
        print("The response of PlatformScreeningTemplatesApi->platform_screening_templates_controller_get_screening_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningTemplatesApi->platform_screening_templates_controller_get_screening_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponseWrapper**](ApiResponseWrapper.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Screening Templates Fetched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

