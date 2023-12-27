# weatherflow_openapi.ObservationsApi

All URIs are relative to *http://swd.weatherflow.com/swd/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_observations_by_device_id**](ObservationsApi.md#get_observations_by_device_id) | **GET** /observations/device/{device_id} | Get Observations for a Single Device
[**get_station_observation**](ObservationsApi.md#get_station_observation) | **GET** /observations/station/{station_id} | Get the latest Station observation


# **get_observations_by_device_id**
> ObservationSet get_observations_by_device_id(device_id, day_offset=day_offset, time_start=time_start, time_end=time_end, format=format)

Get Observations for a Single Device

Get observations for a Device(Air,Sky,Tempest) by using the device_id as the key.  You can find device_id values in the response from the Stations service  You can get observations using several filters (latest, time range, day offset).      Use the \"type\" value to determine the layout of the observations values.  The \"obs\" object is an array of observations.  Each observation is an array of observation values (see layout below).<br><br>**Air**  (type=\"obs_air\")<br>Observation Layout<br>0 - Epoch (seconds UTC)<br>1 - Station Pressure (MB)<br>2 - Air Temperature (C)<br>3 - Relative Humidity (%)<br>4 - Lightning Strike Count<br>5 - Lightning Strike Average Distance (km)<br>6 - Battery (volts)<br>7 - Report Interval (minutes)<br><br>**Sky** (type=\"obs_sky\")<br>Observation Layout<br>0 - Epoch (seconds UTC)<br>1 - Illuminance (lux)<br>2 - UV (index)<br>3 - Rain Accumulation (mm)<br>4 - Wind Lull  (m/s)<br>5 - Wind Avg (m/s)<br>6 - Wind Gust (m/s)<br>7 - Wind Direction (degrees)<br>8 - Battery (volts)<br>9 - Report Interval (minutes)<br>10 - Solar Radiation (W/m^2)<br>11 - Local Day Rain Accumulation (mm)<br>12 - Precipitation Type (0 = none, 1 = rain, 2 = hail, 3 = rain + hail (experimental))<br>13 - Wind Sample Interval (seconds)<br>14 - <a href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a> (mm)<br>15 - Local Day <a href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a> Accumulation (mm)<br>16 - Precipitation Analysis Type (0 = none, 1 = Rain Check with user display on, 2 = Rain Check with user display off)<br><br>**Tempest** (type=\"obs_st\")<br>Observation Layout<br>0 - Epoch (Seconds UTC)<br>1 - Wind Lull  (m/s)<br>2 - Wind Avg (m/s)<br>3 - Wind Gust (m/s)<br>4 - Wind Direction (degrees)<br>5 - Wind Sample Interval (seconds)<br>6 - Pressure (MB)<br>7 - Air Temperature (C)<br>8 - Relative Humidity (%)<br>9 - Illuminance (lux)<br>10 - UV (index)<br>11 - Solar Radiation (W/m^2)<br>12 - Rain Accumulation (mm)<br>13 - Precipitation Type (0 = none, 1 = rain, 2 = hail,  3 = rain + hail (experimental))<br>14 - Average Strike Distance (km)<br>15 - Strike Count<br>16 - Battery (volts)<br>17 - Report Interval (minutes)<br>18 - Local Day Rain Accumulation (mm)<br>19 - <a href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a> Accumulation (mm)<br>20 - Local Day <a href='https://help.weatherflow.com/hc/en-us/articles/360024436634' target='_blank'>NC Rain</a> Accumulation (mm)<br>21 - Precipitation Aanalysis Type (0 = none, 1 = Rain Check with user display on, 2 = Rain Check with user display off)

### Example

* Api Key Authentication (swdApiKey):
* OAuth Authentication (swdImplicit):
```python
import time
import os
import weatherflow_openapi
from weatherflow_openapi.models.observation_set import ObservationSet
from weatherflow_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://swd.weatherflow.com/swd/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = weatherflow_openapi.Configuration(
    host = "http://swd.weatherflow.com/swd/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: swdApiKey
configuration.api_key['swdApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['swdApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with weatherflow_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weatherflow_openapi.ObservationsApi(api_client)
    device_id = 56 # int | ID of device
    day_offset = 56 # int | TIME FILTER - Get an entire day of observations by UTC day offset.<br><br>0 - Current day UTC<br>1 - Yesterday UTC (optional)
    time_start = 56 # int | TIME FILTER - Time range start time epoch seconds UTC.  Observation data at a one minute time resolution is available for a time range that is five days or less.  You also need to send \"time_end\".  This field pair is optional.  If the request does not contain any time filters only the latest observation will be returned. (optional)
    time_end = 56 # int | TIME FILTER - Time range start time epoch seconds UTC.  Observation data at a one minute time resolution is available for a time range that is five days or less.  You also need to send \"time_start\".  This field pair is optional.  If the request does not contain any time filters only the latest observation will be returned. (optional)
    format = 'format_example' # str | Use format=csv to return a CSV response type. (optional)

    try:
        # Get Observations for a Single Device
        api_response = await api_instance.get_observations_by_device_id(device_id, day_offset=day_offset, time_start=time_start, time_end=time_end, format=format)
        print("The response of ObservationsApi->get_observations_by_device_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->get_observations_by_device_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| ID of device | 
 **day_offset** | **int**| TIME FILTER - Get an entire day of observations by UTC day offset.&lt;br&gt;&lt;br&gt;0 - Current day UTC&lt;br&gt;1 - Yesterday UTC | [optional] 
 **time_start** | **int**| TIME FILTER - Time range start time epoch seconds UTC.  Observation data at a one minute time resolution is available for a time range that is five days or less.  You also need to send \&quot;time_end\&quot;.  This field pair is optional.  If the request does not contain any time filters only the latest observation will be returned. | [optional] 
 **time_end** | **int**| TIME FILTER - Time range start time epoch seconds UTC.  Observation data at a one minute time resolution is available for a time range that is five days or less.  You also need to send \&quot;time_start\&quot;.  This field pair is optional.  If the request does not contain any time filters only the latest observation will be returned. | [optional] 
 **format** | **str**| Use format&#x3D;csv to return a CSV response type. | [optional] 

### Return type

[**ObservationSet**](ObservationSet.md)

### Authorization

[swdApiKey](../README.md#swdApiKey), [swdImplicit](../README.md#swdImplicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | Device not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_station_observation**
> StationObservation get_station_observation(station_id)

Get the latest Station observation

Get the latest federated observation for a Station.  This observation is made from the latest Device observations that belong to the Station.  If a user has multiple Devices of the same type they are able to designate one of them as primary. This is the one used to make the federated observation.<br><br>A user can also designate each device as either indoor or outdoor.  All indoor observation value fields will end with an \"_indoor\" suffix.  Outdoor observations fields do not have a suffix.<br><br>The station_units values represent the units of the Station's owner, not the units of the observation values in the API response. 

### Example

* Api Key Authentication (swdApiKey):
* OAuth Authentication (swdImplicit):
```python
import time
import os
import weatherflow_openapi
from weatherflow_openapi.models.station_observation import StationObservation
from weatherflow_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://swd.weatherflow.com/swd/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = weatherflow_openapi.Configuration(
    host = "http://swd.weatherflow.com/swd/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: swdApiKey
configuration.api_key['swdApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['swdApiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with weatherflow_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weatherflow_openapi.ObservationsApi(api_client)
    station_id = 56 # int | ID of Station to return

    try:
        # Get the latest Station observation
        api_response = await api_instance.get_station_observation(station_id)
        print("The response of ObservationsApi->get_station_observation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationsApi->get_station_observation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **int**| ID of Station to return | 

### Return type

[**StationObservation**](StationObservation.md)

### Authorization

[swdApiKey](../README.md#swdApiKey), [swdImplicit](../README.md#swdImplicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | Station not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

