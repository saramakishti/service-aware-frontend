# Entity

## Properties

| Name         | Type       | Description | Notes                                       |
| ------------ | ---------- | ----------- | ------------------------------------------- |
| **did**      | **str**    |             | [optional] [default to 'did:sov:test:1234'] |
| **name**     | **str**    |             | [optional] [default to 'C1']                |
| **ip**       | **str**    |             | [optional] [default to '127.0.0.1']         |
| **visible**  | **bool**   |             | [optional] [default to True]                |
| **other**    | **object** |             | [optional]                                  |
| **attached** | **bool**   |             |

## Example

```python
from openapi_client.models.entity import Entity

# TODO update the JSON string below
json = "{}"
# create an instance of Entity from a JSON string
entity_instance = Entity.from_json(json)
# print the JSON string representation of the object
print Entity.to_json()

# convert the object into a dict
entity_dict = entity_instance.to_dict()
# create an instance of Entity from a dict
entity_form_dict = entity.from_dict(entity_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
