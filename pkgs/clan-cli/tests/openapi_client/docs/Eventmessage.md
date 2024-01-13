# Eventmessage

## Properties

| Name          | Type       | Description | Notes |
| ------------- | ---------- | ----------- | ----- |
| **timestamp** | **int**    |             |
| **group**     | **int**    |             |
| **group_id**  | **int**    |             |
| **msg_type**  | **int**    |             |
| **src_did**   | **str**    |             |
| **des_did**   | **str**    |             |
| **msg**       | **object** |             |
| **id**        | **int**    |             |

## Example

```python
from openapi_client.models.eventmessage import Eventmessage

# TODO update the JSON string below
json = "{}"
# create an instance of Eventmessage from a JSON string
eventmessage_instance = Eventmessage.from_json(json)
# print the JSON string representation of the object
print Eventmessage.to_json()

# convert the object into a dict
eventmessage_dict = eventmessage_instance.to_dict()
# create an instance of Eventmessage from a dict
eventmessage_form_dict = eventmessage.from_dict(eventmessage_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
