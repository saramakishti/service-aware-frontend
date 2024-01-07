# openapi_client.ServicesApi

All URIs are relative to _http://localhost_

| Method                                                          | HTTP request                            | Description          |
| --------------------------------------------------------------- | --------------------------------------- | -------------------- |
| [**create_service**](ServicesApi.md#create_service)             | **POST** /api/v1/service                | Create Service       |
| [**delete_service**](ServicesApi.md#delete_service)             | **DELETE** /api/v1/{entity_did}/service | Delete Service       |
| [**get_all_services**](ServicesApi.md#get_all_services)         | **GET** /api/v1/services                | Get All Services     |
| [**get_service_by_did**](ServicesApi.md#get_service_by_did)     | **GET** /api/v1/{entity_did}/service    | Get Service By Did   |
| [**get_services_by_name**](ServicesApi.md#get_services_by_name) | **GET** /api/v1/services_by_entity_name | Get Services By Name |

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

| Name               | Type                                  | Description | Notes |
| ------------------ | ------------------------------------- | ----------- | ----- |
| **service_create** | [**ServiceCreate**](ServiceCreate.md) |             |

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service**

> Dict[str, str] delete_service(entity_did)

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
    entity_did = 'entity_did_example' # str |

    try:
        # Delete Service
        api_response = api_instance.delete_service(entity_did)
        print("The response of ServicesApi->delete_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
| -------------- | ------- | ----------- | ----- |
| **entity_did** | **str** |             |

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

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

| Name      | Type    | Description | Notes                       |
| --------- | ------- | ----------- | --------------------------- |
| **skip**  | **int** |             | [optional] [default to 0]   |
| **limit** | **int** |             | [optional] [default to 100] |

### Return type

[**List[Service]**](Service.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_by_did**

> List[Service] get_service_by_did(entity_did, skip=skip, limit=limit)

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
    entity_did = 'entity_did_example' # str |
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Service By Did
        api_response = api_instance.get_service_by_did(entity_did, skip=skip, limit=limit)
        print("The response of ServicesApi->get_service_by_did:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_by_did: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes                       |
| -------------- | ------- | ----------- | --------------------------- |
| **entity_did** | **str** |             |
| **skip**       | **int** |             | [optional] [default to 0]   |
| **limit**      | **int** |             | [optional] [default to 100] |

### Return type

[**List[Service]**](Service.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_by_name**

> ServicesByName get_services_by_name(entity_name, skip=skip, limit=limit)

Get Services By Name

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.services_by_name import ServicesByName
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
    entity_name = 'entity_name_example' # str |
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Services By Name
        api_response = api_instance.get_services_by_name(entity_name, skip=skip, limit=limit)
        print("The response of ServicesApi->get_services_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_services_by_name: %s\n" % e)
```

### Parameters

| Name            | Type    | Description | Notes                       |
| --------------- | ------- | ----------- | --------------------------- |
| **entity_name** | **str** |             |
| **skip**        | **int** |             | [optional] [default to 0]   |
| **limit**       | **int** |             | [optional] [default to 100] |

### Return type

[**ServicesByName**](ServicesByName.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **200**     | Successful Response | -                |
| **422**     | Validation Error    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
