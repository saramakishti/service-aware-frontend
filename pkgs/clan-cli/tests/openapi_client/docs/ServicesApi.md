# openapi_client.ServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_service_usage**](ServicesApi.md#add_service_usage) | **POST** /api/v1/service_usage | Add Service Usage
[**create_service**](ServicesApi.md#create_service) | **POST** /api/v1/service | Create Service
[**delete_service**](ServicesApi.md#delete_service) | **DELETE** /api/v1/service | Delete Service
[**get_all_services**](ServicesApi.md#get_all_services) | **GET** /api/v1/services | Get All Services
[**get_service_by_did**](ServicesApi.md#get_service_by_did) | **GET** /api/v1/service_by_did | Get Service By Did
[**get_service_by_uuid**](ServicesApi.md#get_service_by_uuid) | **GET** /api/v1/service | Get Service By Uuid
[**get_services_without_entity**](ServicesApi.md#get_services_without_entity) | **GET** /api/v1/services_without_entity | Get Services Without Entity
[**inc_service_usage**](ServicesApi.md#inc_service_usage) | **PUT** /api/v1/inc_service_usage | Inc Service Usage


# **add_service_usage**
> Service add_service_usage(service_usage_create, service_uuid=service_uuid)

Add Service Usage

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
from openapi_client.models.service_usage_create import ServiceUsageCreate
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
    api_instance = openapi_client.ServicesApi(api_client)
    service_usage_create = openapi_client.ServiceUsageCreate() # ServiceUsageCreate | 
    service_uuid = 'bdd640fb-0667-1ad1-1c80-317fa3b1799d' # str |  (optional) (default to 'bdd640fb-0667-1ad1-1c80-317fa3b1799d')

    try:
        # Add Service Usage
        api_response = api_instance.add_service_usage(service_usage_create, service_uuid=service_uuid)
        print("The response of ServicesApi->add_service_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->add_service_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_usage_create** | [**ServiceUsageCreate**](ServiceUsageCreate.md)|  | 
 **service_uuid** | **str**|  | [optional] [default to &#39;bdd640fb-0667-1ad1-1c80-317fa3b1799d&#39;]

### Return type

[**Service**](Service.md)

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

# **create_service**
> Service create_service(service_create)

Create Service

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
from openapi_client.models.service_create import ServiceCreate
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
    api_instance = openapi_client.ServicesApi(api_client)
    service_create = openapi_client.ServiceCreate() # ServiceCreate | 

    try:
        # Create Service
        api_response = api_instance.create_service(service_create)
        print("The response of ServicesApi->create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->create_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create** | [**ServiceCreate**](ServiceCreate.md)|  | 

### Return type

[**Service**](Service.md)

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

# **delete_service**
> Dict[str, str] delete_service(entity_did=entity_did)

Delete Service

### Example

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ServicesApi(api_client)
    entity_did = 'did:sov:test:120' # str |  (optional) (default to 'did:sov:test:120')

    try:
        # Delete Service
        api_response = api_instance.delete_service(entity_did=entity_did)
        print("The response of ServicesApi->delete_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_did** | **str**|  | [optional] [default to &#39;did:sov:test:120&#39;]

### Return type

**Dict[str, str]**

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

# **get_all_services**
> List[Service] get_all_services(skip=skip, limit=limit)

Get All Services

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
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
    api_instance = openapi_client.ServicesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Services
        api_response = api_instance.get_all_services(skip=skip, limit=limit)
        print("The response of ServicesApi->get_all_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_all_services: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Service]**](Service.md)

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

# **get_service_by_did**
> List[Service] get_service_by_did(entity_did=entity_did, skip=skip, limit=limit)

Get Service By Did

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
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
    api_instance = openapi_client.ServicesApi(api_client)
    entity_did = 'did:sov:test:120' # str |  (optional) (default to 'did:sov:test:120')
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Service By Did
        api_response = api_instance.get_service_by_did(entity_did=entity_did, skip=skip, limit=limit)
        print("The response of ServicesApi->get_service_by_did:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_by_did: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_did** | **str**|  | [optional] [default to &#39;did:sov:test:120&#39;]
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Service]**](Service.md)

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

# **get_service_by_uuid**
> Service get_service_by_uuid(uuid=uuid, skip=skip, limit=limit)

Get Service By Uuid

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
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
    api_instance = openapi_client.ServicesApi(api_client)
    uuid = 'bdd640fb-0667-1ad1-1c80-317fa3b1799d' # str |  (optional) (default to 'bdd640fb-0667-1ad1-1c80-317fa3b1799d')
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Service By Uuid
        api_response = api_instance.get_service_by_uuid(uuid=uuid, skip=skip, limit=limit)
        print("The response of ServicesApi->get_service_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_by_uuid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | [optional] [default to &#39;bdd640fb-0667-1ad1-1c80-317fa3b1799d&#39;]
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**Service**](Service.md)

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

# **get_services_without_entity**
> List[Service] get_services_without_entity(entity_did=entity_did, skip=skip, limit=limit)

Get Services Without Entity

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
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
    api_instance = openapi_client.ServicesApi(api_client)
    entity_did = 'did:sov:test:120' # str |  (optional) (default to 'did:sov:test:120')
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Services Without Entity
        api_response = api_instance.get_services_without_entity(entity_did=entity_did, skip=skip, limit=limit)
        print("The response of ServicesApi->get_services_without_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_services_without_entity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_did** | **str**|  | [optional] [default to &#39;did:sov:test:120&#39;]
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Service]**](Service.md)

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

# **inc_service_usage**
> Service inc_service_usage(service_usage_create, consumer_entity_did=consumer_entity_did, service_uuid=service_uuid)

Inc Service Usage

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.service import Service
from openapi_client.models.service_usage_create import ServiceUsageCreate
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
    api_instance = openapi_client.ServicesApi(api_client)
    service_usage_create = openapi_client.ServiceUsageCreate() # ServiceUsageCreate | 
    consumer_entity_did = 'did:sov:test:120' # str |  (optional) (default to 'did:sov:test:120')
    service_uuid = 'bdd640fb-0667-1ad1-1c80-317fa3b1799d' # str |  (optional) (default to 'bdd640fb-0667-1ad1-1c80-317fa3b1799d')

    try:
        # Inc Service Usage
        api_response = api_instance.inc_service_usage(service_usage_create, consumer_entity_did=consumer_entity_did, service_uuid=service_uuid)
        print("The response of ServicesApi->inc_service_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->inc_service_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_usage_create** | [**ServiceUsageCreate**](ServiceUsageCreate.md)|  | 
 **consumer_entity_did** | **str**|  | [optional] [default to &#39;did:sov:test:120&#39;]
 **service_uuid** | **str**|  | [optional] [default to &#39;bdd640fb-0667-1ad1-1c80-317fa3b1799d&#39;]

### Return type

[**Service**](Service.md)

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

