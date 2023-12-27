# StationUnits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units_temp** | **str** |  | [optional] 
**units_wind** | **str** |  | [optional] 
**units_precip** | **str** |  | [optional] 
**units_pressure** | **str** |  | [optional] 
**units_distance** | **str** |  | [optional] 
**units_direction** | **str** |  | [optional] 
**units_other** | **str** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.station_units import StationUnits

# TODO update the JSON string below
json = "{}"
# create an instance of StationUnits from a JSON string
station_units_instance = StationUnits.from_json(json)
# print the JSON string representation of the object
print StationUnits.to_json()

# convert the object into a dict
station_units_dict = station_units_instance.to_dict()
# create an instance of StationUnits from a dict
station_units_form_dict = station_units.from_dict(station_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


