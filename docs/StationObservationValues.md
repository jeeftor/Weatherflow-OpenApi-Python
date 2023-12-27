# StationObservationValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** |  | [optional] 
**air_temperature** | **float** |  | [optional] 
**barometric_pressure** | **float** |  | [optional] 
**sea_level_pressure** | **float** |  | [optional] 
**relative_humidity** | **float** |  | [optional] 
**precip** | **float** |  | [optional] 
**precip_accum_last_1hr** | **float** |  | [optional] 
**wind_avg** | **float** |  | [optional] 
**wind_direction** | **float** |  | [optional] 
**wind_gust** | **float** |  | [optional] 
**wind_lull** | **float** |  | [optional] 
**solar_radiation** | **float** |  | [optional] 
**uv** | **float** |  | [optional] 
**brightness** | **float** |  | [optional] 
**lightning_strike_last_epoch** | **float** |  | [optional] 
**lightning_strike_last_distance** | **float** |  | [optional] 
**lightning_strike_count_last_3hr** | **float** |  | [optional] 
**feels_like** | **float** |  | [optional] 
**heat_index** | **float** |  | [optional] 
**wind_chill** | **float** |  | [optional] 
**dew_point** | **float** |  | [optional] 
**wet_bulb_temperature** | **float** |  | [optional] 
**delta_t** | **float** |  | [optional] 
**air_density** | **float** |  | [optional] 
**air_temperature_indoor** | **float** |  | [optional] 
**barometric_pressure_indoor** | **float** |  | [optional] 
**sea_level_pressure_indoor** | **float** |  | [optional] 
**relative_humidity_indoor** | **float** |  | [optional] 
**precip_indoor** | **float** |  | [optional] 
**precip_accum_last_1hr_indoor** | **float** |  | [optional] 
**wind_avg_indoor** | **float** |  | [optional] 
**wind_direction_indoor** | **float** |  | [optional] 
**wind_gust_indoor** | **float** |  | [optional] 
**wind_lull_indoor** | **float** |  | [optional] 
**solar_radiation_indoor** | **float** |  | [optional] 
**uv_indoor** | **float** |  | [optional] 
**brightness_indoor** | **float** |  | [optional] 
**lightning_strike_last_epoch_indoor** | **float** |  | [optional] 
**lightning_strike_last_distance_indoor** | **float** |  | [optional] 
**lightning_strike_count_last_3hr_indoor** | **float** |  | [optional] 
**feels_like_indoor** | **float** |  | [optional] 
**heat_index_indoor** | **float** |  | [optional] 
**wind_chill_indoor** | **float** |  | [optional] 
**dew_point_indoor** | **float** |  | [optional] 
**wet_bulb_temperature_indoor** | **float** |  | [optional] 
**delta_t_indoor** | **float** |  | [optional] 
**air_density_indoor** | **float** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.station_observation_values import StationObservationValues

# TODO update the JSON string below
json = "{}"
# create an instance of StationObservationValues from a JSON string
station_observation_values_instance = StationObservationValues.from_json(json)
# print the JSON string representation of the object
print StationObservationValues.to_json()

# convert the object into a dict
station_observation_values_dict = station_observation_values_instance.to_dict()
# create an instance of StationObservationValues from a dict
station_observation_values_form_dict = station_observation_values.from_dict(station_observation_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


