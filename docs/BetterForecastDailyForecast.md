# BetterForecastDailyForecast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_start_local** | **float** |  | [optional] 
**day_num** | **float** |  | [optional] 
**month_num** | **float** |  | [optional] 
**conditions** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**sunrise** | **float** |  | [optional] 
**sunset** | **float** |  | [optional] 
**air_temp_high** | **float** |  | [optional] 
**air_temp_low** | **float** |  | [optional] 
**precip_probability** | **float** |  | [optional] 
**precip_icon** | **str** |  | [optional] 
**precip_type** | **str** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.better_forecast_daily_forecast import BetterForecastDailyForecast

# TODO update the JSON string below
json = "{}"
# create an instance of BetterForecastDailyForecast from a JSON string
better_forecast_daily_forecast_instance = BetterForecastDailyForecast.from_json(json)
# print the JSON string representation of the object
print BetterForecastDailyForecast.to_json()

# convert the object into a dict
better_forecast_daily_forecast_dict = better_forecast_daily_forecast_instance.to_dict()
# create an instance of BetterForecastDailyForecast from a dict
better_forecast_daily_forecast_form_dict = better_forecast_daily_forecast.from_dict(better_forecast_daily_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


