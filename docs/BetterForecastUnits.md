# BetterForecastUnits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units_temp** | **str** |  | [optional] 
**units_wind** | **str** |  | [optional] 
**units_precip** | **str** |  | [optional] 
**units_pressure** | **str** |  | [optional] 
**units_distance** | **str** |  | [optional] 
**units_brightness** | **str** |  | [optional] 
**units_solar_radiation** | **str** |  | [optional] 
**units_other** | **str** |  | [optional] 
**units_air_density** | **str** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.better_forecast_units import BetterForecastUnits

# TODO update the JSON string below
json = "{}"
# create an instance of BetterForecastUnits from a JSON string
better_forecast_units_instance = BetterForecastUnits.from_json(json)
# print the JSON string representation of the object
print BetterForecastUnits.to_json()

# convert the object into a dict
better_forecast_units_dict = better_forecast_units_instance.to_dict()
# create an instance of BetterForecastUnits from a dict
better_forecast_units_form_dict = better_forecast_units.from_dict(better_forecast_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


