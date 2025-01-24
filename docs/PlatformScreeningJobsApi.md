# screening_ai.PlatformScreeningJobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_screening_jobs_controller_create_screening_job**](PlatformScreeningJobsApi.md#platform_screening_jobs_controller_create_screening_job) | **POST** /api/v2/platform/platform-screening-job | Create a new Screening Job
[**platform_screening_jobs_controller_get_screening_job_using_id**](PlatformScreeningJobsApi.md#platform_screening_jobs_controller_get_screening_job_using_id) | **GET** /api/v2/platform/platform-screening-job/id | Get Screening Job using Id
[**platform_screening_jobs_controller_get_screening_jobs_of_org**](PlatformScreeningJobsApi.md#platform_screening_jobs_controller_get_screening_jobs_of_org) | **GET** /api/v2/platform/platform-screening-job/org | Get all Screening Jobs of Organisation


# **platform_screening_jobs_controller_create_screening_job**
> ApiResponseWrapper platform_screening_jobs_controller_create_screening_job(platform_create_screening_job_dto)

Create a new Screening Job

### Example

* Api Key Authentication (X-API-KEY):

```python
import screening_ai
from screening_ai.models.api_response_wrapper import ApiResponseWrapper
from screening_ai.models.platform_create_screening_job_dto import PlatformCreateScreeningJobDto
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
    api_instance = screening_ai.PlatformScreeningJobsApi(api_client)
    platform_create_screening_job_dto = screening_ai.PlatformCreateScreeningJobDto() # PlatformCreateScreeningJobDto | 

    try:
        # Create a new Screening Job
        api_response = api_instance.platform_screening_jobs_controller_create_screening_job(platform_create_screening_job_dto)
        print("The response of PlatformScreeningJobsApi->platform_screening_jobs_controller_create_screening_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningJobsApi->platform_screening_jobs_controller_create_screening_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_create_screening_job_dto** | [**PlatformCreateScreeningJobDto**](PlatformCreateScreeningJobDto.md)|  | 

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
**201** | Screening Job Created Successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_jobs_controller_get_screening_job_using_id**
> ApiResponseWrapper platform_screening_jobs_controller_get_screening_job_using_id(screening_job_id)

Get Screening Job using Id

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
    api_instance = screening_ai.PlatformScreeningJobsApi(api_client)
    screening_job_id = 'screening_job_id_example' # str | Screening Job Id

    try:
        # Get Screening Job using Id
        api_response = api_instance.platform_screening_jobs_controller_get_screening_job_using_id(screening_job_id)
        print("The response of PlatformScreeningJobsApi->platform_screening_jobs_controller_get_screening_job_using_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningJobsApi->platform_screening_jobs_controller_get_screening_job_using_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_job_id** | **str**| Screening Job Id | 

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
**200** | Screening Job Found |  -  |
**404** | No Screening Job Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_screening_jobs_controller_get_screening_jobs_of_org**
> ApiResponseWrapper platform_screening_jobs_controller_get_screening_jobs_of_org()

Get all Screening Jobs of Organisation

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
    api_instance = screening_ai.PlatformScreeningJobsApi(api_client)

    try:
        # Get all Screening Jobs of Organisation
        api_response = api_instance.platform_screening_jobs_controller_get_screening_jobs_of_org()
        print("The response of PlatformScreeningJobsApi->platform_screening_jobs_controller_get_screening_jobs_of_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformScreeningJobsApi->platform_screening_jobs_controller_get_screening_jobs_of_org: %s\n" % e)
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
**200** | Screening Jobs of Organisation |  -  |
**404** | No Screening Jobs Found for Organisation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

