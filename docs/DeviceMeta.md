# DeviceMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agl** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**wifi_network_name** | **str** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.device_meta import DeviceMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceMeta from a JSON string
device_meta_instance = DeviceMeta.from_json(json)
# print the JSON string representation of the object
print DeviceMeta.to_json()

# convert the object into a dict
device_meta_dict = device_meta_instance.to_dict()
# create an instance of DeviceMeta from a dict
device_meta_form_dict = device_meta.from_dict(device_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


