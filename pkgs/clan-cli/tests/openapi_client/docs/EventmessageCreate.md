# EventmessageCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**group** | **int** |  | 
**group_id** | **int** |  | 
**msg_type** | **int** |  | 
**src_did** | **str** |  | 
**des_did** | **str** |  | 
**msg** | **object** |  | 

## Example

```python
from openapi_client.models.eventmessage_create import EventmessageCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EventmessageCreate from a JSON string
eventmessage_create_instance = EventmessageCreate.from_json(json)
# print the JSON string representation of the object
print EventmessageCreate.to_json()

# convert the object into a dict
eventmessage_create_dict = eventmessage_create_instance.to_dict()
# create an instance of EventmessageCreate from a dict
eventmessage_create_form_dict = eventmessage_create.from_dict(eventmessage_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


