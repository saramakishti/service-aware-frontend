# EntityCreate

## Properties

| Name        | Type       | Description | Notes                                       |
| ----------- | ---------- | ----------- | ------------------------------------------- |
| **did**     | **str**    |             | [optional] [default to 'did:sov:test:1234'] |
| **name**    | **str**    |             | [optional] [default to 'C1']                |
| **ip**      | **str**    |             | [optional] [default to '127.0.0.1']         |
| **visible** | **bool**   |             | [optional] [default to True]                |
| **other**   | **object** |             | [optional]                                  |

## Example

```python
from openapi_client.models.entity_create import EntityCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCreate from a JSON string
entity_create_instance = EntityCreate.from_json(json)
# print the JSON string representation of the object
print EntityCreate.to_json()

# convert the object into a dict
entity_create_dict = entity_create_instance.to_dict()
# create an instance of EntityCreate from a dict
entity_create_form_dict = entity_create.from_dict(entity_create_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
