# screening_ai.PlatformScreeningSubmissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_screening_submissions_controller_convert_audio_to_text**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_convert_audio_to_text) | **POST** /api/v2/platform/platform-screening-submission/textFromAudio | Convert Audio to Text
[**platform_screening_submissions_controller_create_screening_stream_room**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_create_screening_stream_room) | **POST** /api/v2/platform/platform-screening-submission/stream/start | Create Screening Submission Streaming Room
[**platform_screening_submissions_controller_create_screening_submission**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_create_screening_submission) | **POST** /api/v2/platform/platform-screening-submission | Create a new Screening Submission
[**platform_screening_submissions_controller_get_screening_submission_using_id**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_get_screening_submission_using_id) | **GET** /api/v2/platform/platform-screening-submission/id | Get Screening Submission using ID
[**platform_screening_submissions_controller_get_screening_submissions_of_org**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_get_screening_submissions_of_org) | **POST** /api/v2/platform/platform-screening-submission/org/filters | Get Screening Submissions of an Organisation
[**platform_screening_submissions_controller_get_screening_submissions_using_email_phone**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_get_screening_submissions_using_email_phone) | **GET** /api/v2/platform/platform-screening-submission/email-phone | Get Screening Submission using Email ir Phone
[**platform_screening_submissions_controller_get_screening_submissions_using_job_id**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_get_screening_submissions_using_job_id) | **GET** /api/v2/platform/platform-screening-submission/jobId | Get Screening Submissions using Job ID
[**platform_screening_submissions_controller_update_screening_submission_chat**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_update_screening_submission_chat) | **PUT** /api/v2/platform/platform-screening-submission | Update Screening Submission Chat Objects
[**platform_screening_submissions_controller_update_screening_submission_status**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_update_screening_submission_status) | **PUT** /api/v2/platform/platform-screening-submission/status | Update Screening Submission Status
[**platform_screening_submissions_controller_update_screening_submission_view_status**](PlatformScreeningSubmissionsApi.md#platform_screening_submissions_controller_update_screening_submission_view_status) | **PUT** /api/v2/platform/platform-screening-submission/view | Update Screening Submission View Status


# **platform_screening_submissions_controller_convert_audio_to_text**
> ApiResponseWrapper platform_screening_submissions_controller_convert_audio_to_text(org_id, screening_submission_id, index, file, file_type)

Convert Audio to Text

### Example


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


# Enter a context with an instance of the API client
with screening_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    org_id = 'org_id_example' # str | Organisation ID
    screening_submission_id = 'screening_submission_id_example' # str | Screening Submission ID
    index = 3.4 # float | Index of the question
    file = None # bytearray | The audio file of the answer
    file_type = 'file_type_example' # str | File Type

    try:
        # Convert Audio to Text
        api_response = api_instance.platform_screening_submissions_controller_convert_audio_to_text(org_id, screening_submission_id, index, file, file_type)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_convert_audio_to_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_convert_audio_to_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organisation ID | 
 **screening_submission_id** | **str**| Screening Submission ID | 
 **index** | **float**| Index of the question | 
 **file** | **bytearray**| The audio file of the answer | 
 **file_type** | **str**| File Type | 

### Return type

[**ApiResponseWrapper**](ApiResponseWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Text from Audio |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_create_screening_stream_room**
> ApiResponseWrapper platform_screening_submissions_controller_create_screening_stream_room(create_platform_screening_submission_streaming_room_token_dto)

Create Screening Submission Streaming Room

### Example


```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.models.create_platform_screening_submission_streaming_room_token_dto import CreatePlatformScreeningSubmissionStreamingRoomTokenDto
from screening_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = screening_ai.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with screening_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    create_platform_screening_submission_streaming_room_token_dto = screening_ai.CreatePlatformScreeningSubmissionStreamingRoomTokenDto() # CreatePlatformScreeningSubmissionStreamingRoomTokenDto | 

    try:
        # Create Screening Submission Streaming Room
        api_response = api_instance.platform_screening_submissions_controller_create_screening_stream_room(create_platform_screening_submission_streaming_room_token_dto)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_create_screening_stream_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_create_screening_stream_room: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_platform_screening_submission_streaming_room_token_dto** | [**CreatePlatformScreeningSubmissionStreamingRoomTokenDto**](CreatePlatformScreeningSubmissionStreamingRoomTokenDto.md)|  | 

### Return type

[**ApiResponseWrapper**](ApiResponseWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Screening Submission Streaming Room Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_create_screening_submission**
> ApiResponseWrapper platform_screening_submissions_controller_create_screening_submission(create_platform_screening_form_submission_dto)

Create a new Screening Submission

### Example


```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.models.create_platform_screening_form_submission_dto import CreatePlatformScreeningFormSubmissionDto
from screening_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = screening_ai.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with screening_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    create_platform_screening_form_submission_dto = screening_ai.CreatePlatformScreeningFormSubmissionDto() # CreatePlatformScreeningFormSubmissionDto | 

    try:
        # Create a new Screening Submission
        api_response = api_instance.platform_screening_submissions_controller_create_screening_submission(create_platform_screening_form_submission_dto)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_create_screening_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_create_screening_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_platform_screening_form_submission_dto** | [**CreatePlatformScreeningFormSubmissionDto**](CreatePlatformScreeningFormSubmissionDto.md)|  | 

### Return type

[**ApiResponseWrapper**](ApiResponseWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Screening Submission Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_get_screening_submission_using_id**
> ApiResponseWrapper platform_screening_submissions_controller_get_screening_submission_using_id(screening_submission_id)

Get Screening Submission using ID

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
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    screening_submission_id = 'screening_submission_id_example' # str | Screening Submission ID

    try:
        # Get Screening Submission using ID
        api_response = api_instance.platform_screening_submissions_controller_get_screening_submission_using_id(screening_submission_id)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_get_screening_submission_using_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_get_screening_submission_using_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_submission_id** | **str**| Screening Submission ID | 

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
**200** | Screening Submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_get_screening_submissions_of_org**
> ApiResponseWrapper platform_screening_submissions_controller_get_screening_submissions_of_org(get_platform_screening_submissions_of_org_dto)

Get Screening Submissions of an Organisation

### Example

* Api Key Authentication (X-API-KEY):

```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.models.get_platform_screening_submissions_of_org_dto import GetPlatformScreeningSubmissionsOfOrgDto
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
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    get_platform_screening_submissions_of_org_dto = screening_ai.GetPlatformScreeningSubmissionsOfOrgDto() # GetPlatformScreeningSubmissionsOfOrgDto | 

    try:
        # Get Screening Submissions of an Organisation
        api_response = api_instance.platform_screening_submissions_controller_get_screening_submissions_of_org(get_platform_screening_submissions_of_org_dto)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_get_screening_submissions_of_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_get_screening_submissions_of_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_platform_screening_submissions_of_org_dto** | [**GetPlatformScreeningSubmissionsOfOrgDto**](GetPlatformScreeningSubmissionsOfOrgDto.md)|  | 

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
**200** | Screening Submissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_get_screening_submissions_using_email_phone**
> ApiResponseWrapper platform_screening_submissions_controller_get_screening_submissions_using_email_phone(email, phone, org_alias, job_id)

Get Screening Submission using Email ir Phone

### Example


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


# Enter a context with an instance of the API client
with screening_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    email = 'email_example' # str | Email
    phone = 'phone_example' # str | Phone Number
    org_alias = 'org_alias_example' # str | Organisation Alias
    job_id = 'job_id_example' # str | Job ID

    try:
        # Get Screening Submission using Email ir Phone
        api_response = api_instance.platform_screening_submissions_controller_get_screening_submissions_using_email_phone(email, phone, org_alias, job_id)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_get_screening_submissions_using_email_phone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_get_screening_submissions_using_email_phone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email | 
 **phone** | **str**| Phone Number | 
 **org_alias** | **str**| Organisation Alias | 
 **job_id** | **str**| Job ID | 

### Return type

[**ApiResponseWrapper**](ApiResponseWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Screening Submission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_get_screening_submissions_using_job_id**
> ApiResponseWrapper platform_screening_submissions_controller_get_screening_submissions_using_job_id(job_id)

Get Screening Submissions using Job ID

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
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    job_id = 'job_id_example' # str | Job ID

    try:
        # Get Screening Submissions using Job ID
        api_response = api_instance.platform_screening_submissions_controller_get_screening_submissions_using_job_id(job_id)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_get_screening_submissions_using_job_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_get_screening_submissions_using_job_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

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
**200** | Screening Submissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_update_screening_submission_chat**
> ApiResponseWrapper platform_screening_submissions_controller_update_screening_submission_chat(update_platform_screening_submission_chat_dto)

Update Screening Submission Chat Objects

### Example


```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.models.update_platform_screening_submission_chat_dto import UpdatePlatformScreeningSubmissionChatDto
from screening_ai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = screening_ai.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with screening_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    update_platform_screening_submission_chat_dto = screening_ai.UpdatePlatformScreeningSubmissionChatDto() # UpdatePlatformScreeningSubmissionChatDto | 

    try:
        # Update Screening Submission Chat Objects
        api_response = api_instance.platform_screening_submissions_controller_update_screening_submission_chat(update_platform_screening_submission_chat_dto)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_update_screening_submission_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_update_screening_submission_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_platform_screening_submission_chat_dto** | [**UpdatePlatformScreeningSubmissionChatDto**](UpdatePlatformScreeningSubmissionChatDto.md)|  | 

### Return type

[**ApiResponseWrapper**](ApiResponseWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Screening Submission Chat Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_update_screening_submission_status**
> ApiResponseWrapper platform_screening_submissions_controller_update_screening_submission_status(update_platform_screening_submissions_status_dto)

Update Screening Submission Status

### Example

* Api Key Authentication (X-API-KEY):

```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.models.update_platform_screening_submissions_status_dto import UpdatePlatformScreeningSubmissionsStatusDto
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
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    update_platform_screening_submissions_status_dto = screening_ai.UpdatePlatformScreeningSubmissionsStatusDto() # UpdatePlatformScreeningSubmissionsStatusDto | 

    try:
        # Update Screening Submission Status
        api_response = api_instance.platform_screening_submissions_controller_update_screening_submission_status(update_platform_screening_submissions_status_dto)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_update_screening_submission_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_update_screening_submission_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_platform_screening_submissions_status_dto** | [**UpdatePlatformScreeningSubmissionsStatusDto**](UpdatePlatformScreeningSubmissionsStatusDto.md)|  | 

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
**200** | Screening Submission Status Updated |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_submissions_controller_update_screening_submission_view_status**
> ApiResponseWrapper platform_screening_submissions_controller_update_screening_submission_view_status(screening_submission_id)

Update Screening Submission View Status

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
    api_instance = screening_ai.PlatformScreeningSubmissionsApi(api_client)
    screening_submission_id = 'screening_submission_id_example' # str | Screening Submission ID

    try:
        # Update Screening Submission View Status
        api_response = api_instance.platform_screening_submissions_controller_update_screening_submission_view_status(screening_submission_id)
        print("The response of PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_update_screening_submission_view_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningSubmissionsApi->platform_screening_submissions_controller_update_screening_submission_view_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_submission_id** | **str**| Screening Submission ID | 

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
**200** | Screening Submission View Status Updated |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

