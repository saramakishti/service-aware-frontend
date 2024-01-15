# openapi_client.ResolutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_resolutions**](ResolutionApi.md#get_all_resolutions) | **GET** /api/v1/resolutions | Get All Resolutions


# **get_all_resolutions**
> List[Resolution] get_all_resolutions(skip=skip, limit=limit)

Get All Resolutions

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.resolution import Resolution
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResolutionApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Resolutions
        api_response = api_instance.get_all_resolutions(skip=skip, limit=limit)
        print("The response of ResolutionApi->get_all_resolutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResolutionApi->get_all_resolutions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Resolution]**](Resolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

