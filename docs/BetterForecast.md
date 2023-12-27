# BetterForecast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**current_conditions** | [**BetterForecastCurrentConditions**](BetterForecastCurrentConditions.md) |  | [optional] 
**forecast** | [**BetterForecastForecast**](BetterForecastForecast.md) |  | [optional] 
**units** | [**BetterForecastUnits**](BetterForecastUnits.md) |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**timezone** | **str** |  | [optional] 
**timezone_offset_minutes** | **float** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.better_forecast import BetterForecast

# TODO update the JSON string below
json = "{}"
# create an instance of BetterForecast from a JSON string
better_forecast_instance = BetterForecast.from_json(json)
# print the JSON string representation of the object
print BetterForecast.to_json()

# convert the object into a dict
better_forecast_dict = better_forecast_instance.to_dict()
# create an instance of BetterForecast from a dict
better_forecast_form_dict = better_forecast.from_dict(better_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


