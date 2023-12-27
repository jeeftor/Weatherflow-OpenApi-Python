# ObservationSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**device_id** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**obs** | **List[List[float]]** |  | [optional] 

## Example

```python
from weatherflow_openapi.models.observation_set import ObservationSet

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationSet from a JSON string
observation_set_instance = ObservationSet.from_json(json)
# print the JSON string representation of the object
print ObservationSet.to_json()

# convert the object into a dict
observation_set_dict = observation_set_instance.to_dict()
# create an instance of ObservationSet from a dict
observation_set_form_dict = observation_set.from_dict(observation_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


