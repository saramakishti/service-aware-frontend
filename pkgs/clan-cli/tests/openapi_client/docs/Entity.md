# Entity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**did** | **str** |  | 
**name** | **str** |  | 
**ip** | **str** |  | 
**network** | **str** |  | 
**visible** | **bool** |  | 
**other** | **object** |  | 
**attached** | **bool** |  | 
**stop_health_task** | **bool** |  | 
**roles** | [**List[Role]**](Role.md) |  | 

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


