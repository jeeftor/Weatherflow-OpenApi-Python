# StationMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elevation** | **float** |  | [optional] 
**share_with_wf** | **bool** |  | [optional] [default to True]
**share_with_wu** | **bool** |  | [optional] [default to True]

## Example

```python
from weatherflow_openapi.models.station_meta import StationMeta

# TODO update the JSON string below
json = "{}"
# create an instance of StationMeta from a JSON string
station_meta_instance = StationMeta.from_json(json)
# print the JSON string representation of the object
print StationMeta.to_json()

# convert the object into a dict
station_meta_dict = station_meta_instance.to_dict()
# create an instance of StationMeta from a dict
station_meta_form_dict = station_meta.from_dict(station_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


