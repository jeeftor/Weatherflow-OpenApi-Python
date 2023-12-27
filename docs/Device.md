# Device


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**device_meta** | [**DeviceMeta**](DeviceMeta.md) |  | [optional] 
**device_type** | **str** |  | [optional] 
**hardware_revision** | **str** |  | [optional] 
**firmware_revision** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print Device.to_json()

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_form_dict = device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


