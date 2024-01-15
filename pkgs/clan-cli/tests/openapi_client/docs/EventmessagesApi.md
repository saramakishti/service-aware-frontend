# openapi_client.EventmessagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eventmessage**](EventmessagesApi.md#create_eventmessage) | **POST** /api/v1/event_message | Create Eventmessage
[**get_all_eventmessages**](EventmessagesApi.md#get_all_eventmessages) | **GET** /api/v1/event_messages | Get All Eventmessages


# **create_eventmessage**
> Eventmessage create_eventmessage(eventmessage_create)

Create Eventmessage

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.eventmessage import Eventmessage
from openapi_client.models.eventmessage_create import EventmessageCreate
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
    api_instance = openapi_client.EventmessagesApi(api_client)
    eventmessage_create = openapi_client.EventmessageCreate() # EventmessageCreate | 

    try:
        # Create Eventmessage
        api_response = api_instance.create_eventmessage(eventmessage_create)
        print("The response of EventmessagesApi->create_eventmessage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventmessagesApi->create_eventmessage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eventmessage_create** | [**EventmessageCreate**](EventmessageCreate.md)|  | 

### Return type

[**Eventmessage**](Eventmessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_eventmessages**
> List[Eventmessage] get_all_eventmessages(skip=skip, limit=limit)

Get All Eventmessages

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.eventmessage import Eventmessage
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
    api_instance = openapi_client.EventmessagesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Eventmessages
        api_response = api_instance.get_all_eventmessages(skip=skip, limit=limit)
        print("The response of EventmessagesApi->get_all_eventmessages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventmessagesApi->get_all_eventmessages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Eventmessage]**](Eventmessage.md)

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

