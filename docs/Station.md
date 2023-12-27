# Station


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**station_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**station_meta** | [**StationMeta**](StationMeta.md) |  | [optional] 
**devices** | [**List[Device]**](Device.md) |  | [optional] 
**station_items** | [**List[StationItem]**](StationItem.md) |  | [optional] 

## Example

```python
from weatherflow_openapi.models.station import Station

# TODO update the JSON string below
json = "{}"
# create an instance of Station from a JSON string
station_instance = Station.from_json(json)
# print the JSON string representation of the object
print Station.to_json()

# convert the object into a dict
station_dict = station_instance.to_dict()
# create an instance of Station from a dict
station_form_dict = station.from_dict(station_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


