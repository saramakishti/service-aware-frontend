# openapi_client.RepositoriesApi

All URIs are relative to _http://localhost_

| Method                                                              | HTTP request                 | Description          |
| ------------------------------------------------------------------- | ---------------------------- | -------------------- |
| [**get_all_repositories**](RepositoriesApi.md#get_all_repositories) | **GET** /api/v1/repositories | Get All Repositories |

# **get_all_repositories**

> List[Service] get_all_repositories(skip=skip, limit=limit)

Get All Repositories

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
    api_instance = openapi_client.RepositoriesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get All Repositories
        api_response = api_instance.get_all_repositories(skip=skip, limit=limit)
        print("The response of RepositoriesApi->get_all_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_all_repositories: %s\n" % e)
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
