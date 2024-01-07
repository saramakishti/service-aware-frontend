# openapi_client.EntitiesApi

All URIs are relative to _http://localhost_

| Method                                                            | HTTP request                           | Description           |
| ----------------------------------------------------------------- | -------------------------------------- | --------------------- |
| [**attach_entity**](EntitiesApi.md#attach_entity)                 | **POST** /api/v1/{entity_did}/attach   | Attach Entity         |
| [**create_entity**](EntitiesApi.md#create_entity)                 | **POST** /api/v1/entity                | Create Entity         |
| [**delete_entity**](EntitiesApi.md#delete_entity)                 | **DELETE** /api/v1/{entity_did}/entity | Delete Entity         |
| [**detach_entity**](EntitiesApi.md#detach_entity)                 | **POST** /api/v1/{entity_did}/detach   | Detach Entity         |
| [**get_all_entities**](EntitiesApi.md#get_all_entities)           | **GET** /api/v1/entities               | Get All Entities      |
| [**get_attached_entities**](EntitiesApi.md#get_attached_entities) | **GET** /api/v1/attached_entities      | Get Attached Entities |
| [**get_entity_by_did**](EntitiesApi.md#get_entity_by_did)         | **GET** /api/v1/{entity_did}/entity    | Get Entity By Did     |
| [**get_entity_by_name**](EntitiesApi.md#get_entity_by_name)       | **GET** /api/v1/entity_by_name         | Get Entity By Name    |

# **attach_entity**

> Dict[str, str] attach_entity(entity_did, skip=skip, limit=limit)

Attach Entity

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
    api_instance = openapi_client.EntitiesApi(api_client)
    entity_did = 'entity_did_example' # str |
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Attach Entity
        api_response = api_instance.attach_entity(entity_did, skip=skip, limit=limit)
        print("The response of EntitiesApi->attach_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->attach_entity: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes                       |
| -------------- | ------- | ----------- | --------------------------- |
| **entity_did** | **str** |             |
| **skip**       | **int** |             | [optional] [default to 0]   |
| **limit**      | **int** |             | [optional] [default to 100] |

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

# **create_entity**

> Entity create_entity(entity_create)

Create Entity

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entity import Entity
from openapi_client.models.entity_create import EntityCreate
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
    api_instance = openapi_client.EntitiesApi(api_client)
    entity_create = openapi_client.EntityCreate() # EntityCreate |

    try:
        # Create Entity
        api_response = api_instance.create_entity(entity_create)
        print("The response of EntitiesApi->create_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->create_entity: %s\n" % e)
```

### Parameters

| Name              | Type                                | Description | Notes |
| ----------------- | ----------------------------------- | ----------- | ----- |
| **entity_create** | [**EntityCreate**](EntityCreate.md) |             |

### Return type

[**Entity**](Entity.md)

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

# **delete_entity**

> Dict[str, str] delete_entity(entity_did)

Delete Entity

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
    api_instance = openapi_client.EntitiesApi(api_client)
    entity_did = 'entity_did_example' # str |

    try:
        # Delete Entity
        api_response = api_instance.delete_entity(entity_did)
        print("The response of EntitiesApi->delete_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->delete_entity: %s\n" % e)
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

# **detach_entity**

> Entity detach_entity(entity_did, skip=skip, limit=limit)

Detach Entity

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entity import Entity
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
    api_instance = openapi_client.EntitiesApi(api_client)
    entity_did = 'entity_did_example' # str |
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Detach Entity
        api_response = api_instance.detach_entity(entity_did, skip=skip, limit=limit)
        print("The response of EntitiesApi->detach_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->detach_entity: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes                       |
| -------------- | ------- | ----------- | --------------------------- |
| **entity_did** | **str** |             |
| **skip**       | **int** |             | [optional] [default to 0]   |
| **limit**      | **int** |             | [optional] [default to 100] |

### Return type

[**Entity**](Entity.md)

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

# **get_all_entities**

> List[Entity] get_all_entities(skip=skip, limit=limit)

Get All Entities

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entity import Entity
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
    api_instance = openapi_client.EntitiesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Entities
        api_response = api_instance.get_all_entities(skip=skip, limit=limit)
        print("The response of EntitiesApi->get_all_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_all_entities: %s\n" % e)
```

### Parameters

| Name      | Type    | Description | Notes                       |
| --------- | ------- | ----------- | --------------------------- |
| **skip**  | **int** |             | [optional] [default to 0]   |
| **limit** | **int** |             | [optional] [default to 100] |

### Return type

[**List[Entity]**](Entity.md)

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

# **get_attached_entities**

> List[Entity] get_attached_entities(skip=skip, limit=limit)

Get Attached Entities

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entity import Entity
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
    api_instance = openapi_client.EntitiesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Attached Entities
        api_response = api_instance.get_attached_entities(skip=skip, limit=limit)
        print("The response of EntitiesApi->get_attached_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_attached_entities: %s\n" % e)
```

### Parameters

| Name      | Type    | Description | Notes                       |
| --------- | ------- | ----------- | --------------------------- |
| **skip**  | **int** |             | [optional] [default to 0]   |
| **limit** | **int** |             | [optional] [default to 100] |

### Return type

[**List[Entity]**](Entity.md)

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

# **get_entity_by_did**

> Entity get_entity_by_did(entity_did)

Get Entity By Did

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entity import Entity
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
    api_instance = openapi_client.EntitiesApi(api_client)
    entity_did = 'entity_did_example' # str |

    try:
        # Get Entity By Did
        api_response = api_instance.get_entity_by_did(entity_did)
        print("The response of EntitiesApi->get_entity_by_did:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity_by_did: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
| -------------- | ------- | ----------- | ----- |
| **entity_did** | **str** |             |

### Return type

[**Entity**](Entity.md)

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

# **get_entity_by_name**

> Entity get_entity_by_name(entity_name)

Get Entity By Name

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entity import Entity
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
    api_instance = openapi_client.EntitiesApi(api_client)
    entity_name = 'entity_name_example' # str |

    try:
        # Get Entity By Name
        api_response = api_instance.get_entity_by_name(entity_name)
        print("The response of EntitiesApi->get_entity_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity_by_name: %s\n" % e)
```

### Parameters

| Name            | Type    | Description | Notes |
| --------------- | ------- | ----------- | ----- |
| **entity_name** | **str** |             |

### Return type

[**Entity**](Entity.md)

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
