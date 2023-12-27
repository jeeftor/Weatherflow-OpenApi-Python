# StationObservation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**station_units** | [**StationUnits**](StationUnits.md) |  | [optional] 
**station_id** | **int** |  | [optional] 
**station_name** | **str** |  | [optional] 
**public_name** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**timezone** | **str** |  | [optional] 
**elevation** | **float** |  | [optional] 
**obs** | [**List[StationObservationValues]**](StationObservationValues.md) |  | [optional] 

## Example

```python
from weatherflow_openapi.models.station_observation import StationObservation

# TODO update the JSON string below
json = "{}"
# create an instance of StationObservation from a JSON string
station_observation_instance = StationObservation.from_json(json)
# print the JSON string representation of the object
print StationObservation.to_json()

# convert the object into a dict
station_observation_dict = station_observation_instance.to_dict()
# create an instance of StationObservation from a dict
station_observation_form_dict = station_observation.from_dict(station_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


