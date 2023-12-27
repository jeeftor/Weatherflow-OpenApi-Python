# BetterForecastForecast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**List[BetterForecastDailyForecast]**](BetterForecastDailyForecast.md) |  | [optional] 
**hourly** | [**List[BetterForecastHourlyForecast]**](BetterForecastHourlyForecast.md) |  | [optional] 

## Example

```python
from weatherflow_openapi.models.better_forecast_forecast import BetterForecastForecast

# TODO update the JSON string below
json = "{}"
# create an instance of BetterForecastForecast from a JSON string
better_forecast_forecast_instance = BetterForecastForecast.from_json(json)
# print the JSON string representation of the object
print BetterForecastForecast.to_json()

# convert the object into a dict
better_forecast_forecast_dict = better_forecast_forecast_instance.to_dict()
# create an instance of BetterForecastForecast from a dict
better_forecast_forecast_form_dict = better_forecast_forecast.from_dict(better_forecast_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


