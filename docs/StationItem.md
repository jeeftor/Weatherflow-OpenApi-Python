# StationItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_item_id** | **int** |  | [optional] 
**station_id** | **int** |  | [optional] 
**device_id** | **int** |  | [optional] 
**item** | **str** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.station_item import StationItem

# TODO update the JSON string below
json = "{}"
# create an instance of StationItem from a JSON string
station_item_instance = StationItem.from_json(json)
# print the JSON string representation of the object
print StationItem.to_json()

# convert the object into a dict
station_item_dict = station_item_instance.to_dict()
# create an instance of StationItem from a dict
station_item_form_dict = station_item.from_dict(station_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


