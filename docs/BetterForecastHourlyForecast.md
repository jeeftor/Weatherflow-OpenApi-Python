# BetterForecastHourlyForecast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** |  | [optional] 
**conditions** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**air_temperature** | **float** |  | [optional] 
**sea_level_pressure** | **float** |  | [optional] 
**relative_humidity** | **float** |  | [optional] 
**precip** | **float** |  | [optional] 
**precip_probability** | **float** |  | [optional] 
**wind_avg** | **float** |  | [optional] 
**wind_direction** | **float** |  | [optional] 
**wind_direction_cardinal** | **str** |  | [optional] 
**wind_gust** | **float** |  | [optional] 
**uv** | **float** |  | [optional] 
**feels_like** | **float** |  | [optional] 
**local_hour** | **float** |  | [optional] 
**local_day** | **float** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.better_forecast_hourly_forecast import BetterForecastHourlyForecast

# TODO update the JSON string below
json = "{}"
# create an instance of BetterForecastHourlyForecast from a JSON string
better_forecast_hourly_forecast_instance = BetterForecastHourlyForecast.from_json(json)
# print the JSON string representation of the object
print BetterForecastHourlyForecast.to_json()

# convert the object into a dict
better_forecast_hourly_forecast_dict = better_forecast_hourly_forecast_instance.to_dict()
# create an instance of BetterForecastHourlyForecast from a dict
better_forecast_hourly_forecast_form_dict = better_forecast_hourly_forecast.from_dict(better_forecast_hourly_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


