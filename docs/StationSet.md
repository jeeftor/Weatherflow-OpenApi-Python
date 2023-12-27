# StationSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**locations** | [**List[Station]**](Station.md) |  | [optional] 

## Example

```python
from weatherflow_openapi.models.station_set import StationSet

# TODO update the JSON string below
json = "{}"
# create an instance of StationSet from a JSON string
station_set_instance = StationSet.from_json(json)
# print the JSON string representation of the object
print StationSet.to_json()

# convert the object into a dict
station_set_dict = station_set_instance.to_dict()
# create an instance of StationSet from a dict
station_set_form_dict = station_set.from_dict(station_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


