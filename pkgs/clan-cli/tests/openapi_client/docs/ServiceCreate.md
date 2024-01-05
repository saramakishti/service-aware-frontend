# ServiceCreate

## Properties

| Name             | Type       | Description | Notes                                                          |
| ---------------- | ---------- | ----------- | -------------------------------------------------------------- |
| **uuid**         | **str**    |             | [optional] [default to '8e285c0c-4e40-430a-a477-26b3b81e30df'] |
| **service_name** | **str**    |             | [optional] [default to 'Carlos Printing']                      |
| **service_type** | **str**    |             | [optional] [default to '3D Printing']                          |
| **endpoint_url** | **str**    |             | [optional] [default to 'http://127.0.0.1:8000']                |
| **status**       | **str**    |             | [optional] [default to 'unknown']                              |
| **other**        | **object** |             | [optional]                                                     |
| **entity_did**   | **str**    |             | [optional] [default to 'did:sov:test:1234']                    |

## Example

```python
from openapi_client.models.service_create import ServiceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreate from a JSON string
service_create_instance = ServiceCreate.from_json(json)
# print the JSON string representation of the object
print ServiceCreate.to_json()

# convert the object into a dict
service_create_dict = service_create_instance.to_dict()
# create an instance of ServiceCreate from a dict
service_create_form_dict = service_create.from_dict(service_create_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
