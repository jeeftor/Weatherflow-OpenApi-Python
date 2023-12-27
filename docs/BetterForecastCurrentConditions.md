# BetterForecastCurrentConditions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** |  | [optional] 
**conditions** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**air_temperature** | **float** |  | [optional] 
**sea_level_pressure** | **float** |  | [optional] 
**station_pressure** | **float** |  | [optional] 
**pressure_trend** | **str** |  | [optional] 
**relative_humidity** | **float** |  | [optional] 
**wind_avg** | **float** |  | [optional] 
**wind_direction** | **float** |  | [optional] 
**wind_direction_cardinal** | **str** |  | [optional] 
**wind_direction_icon** | **str** |  | [optional] 
**wind_gust** | **float** |  | [optional] 
**solar_radiation** | **float** |  | [optional] 
**uv** | **float** |  | [optional] 
**brightness** | **float** |  | [optional] 
**feels_like** | **float** |  | [optional] 
**dew_point** | **float** |  | [optional] 
**wet_bulb_temperature** | **float** |  | [optional] 
**delta_t** | **float** |  | [optional] 
**air_density** | **float** |  | [optional] 
**lightning_strike_count_last_1hr** | **float** |  | [optional] 
**lightning_strike_count_last_3hr** | **float** |  | [optional] 
**lightning_strike_last_distance** | **float** |  | [optional] 
**lightning_strike_last_distance_msg** | **str** |  | [optional] 
**lightning_strike_last_epoch** | **float** |  | [optional] 
**precip_accum_local_day** | **float** |  | [optional] 
**precip_accum_local_yesterday** | **float** |  | [optional] 
**precip_minutes_local_day** | **float** |  | [optional] 
**precip_minutes_local_yesterday** | **float** |  | [optional] 
**is_precip_local_day_rain_check** | **bool** |  | [optional] 
**is_precip_local_yesterday_rain_check** | **float** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.better_forecast_current_conditions import BetterForecastCurrentConditions

# TODO update the JSON string below
json = "{}"
# create an instance of BetterForecastCurrentConditions from a JSON string
better_forecast_current_conditions_instance = BetterForecastCurrentConditions.from_json(json)
# print the JSON string representation of the object
print BetterForecastCurrentConditions.to_json()

# convert the object into a dict
better_forecast_current_conditions_dict = better_forecast_current_conditions_instance.to_dict()
# create an instance of BetterForecastCurrentConditions from a dict
better_forecast_current_conditions_form_dict = better_forecast_current_conditions.from_dict(better_forecast_current_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


