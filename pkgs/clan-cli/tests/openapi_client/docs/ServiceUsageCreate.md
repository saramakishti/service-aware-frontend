# ServiceUsageCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**times_consumed** | **int** |  | 
**consumer_entity_did** | **str** |  | 

## Example

```python
from openapi_client.models.service_usage_create import ServiceUsageCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUsageCreate from a JSON string
service_usage_create_instance = ServiceUsageCreate.from_json(json)
# print the JSON string representation of the object
print ServiceUsageCreate.to_json()

# convert the object into a dict
service_usage_create_dict = service_usage_create_instance.to_dict()
# create an instance of ServiceUsageCreate from a dict
service_usage_create_form_dict = service_usage_create.from_dict(service_usage_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


