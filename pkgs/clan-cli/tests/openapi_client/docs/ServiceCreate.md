# ServiceCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**service_name** | **str** |  | 
**service_type** | **str** |  | 
**endpoint_url** | **str** |  | 
**status** | **str** |  | 
**other** | **object** |  | 
**entity_did** | **str** |  | 

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


