# ServicesByName

## Properties

| Name         | Type                            | Description | Notes |
| ------------ | ------------------------------- | ----------- | ----- |
| **entity**   | [**Entity**](Entity.md)         |             |
| **services** | [**List[Service]**](Service.md) |             |

## Example

```python
from openapi_client.models.services_by_name import ServicesByName

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesByName from a JSON string
services_by_name_instance = ServicesByName.from_json(json)
# print the JSON string representation of the object
print ServicesByName.to_json()

# convert the object into a dict
services_by_name_dict = services_by_name_instance.to_dict()
# create an instance of ServicesByName from a dict
services_by_name_form_dict = services_by_name.from_dict(services_by_name_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
