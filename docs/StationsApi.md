# weatherflow_openapi.StationsApi

All URIs are relative to *http://swd.weatherflow.com/swd/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_station_by_id**](StationsApi.md#get_station_by_id) | **GET** /stations/{station_id} | Find a Station by station_id
[**get_stations**](StationsApi.md#get_stations) | **GET** /stations | Find all Stations for a user


# **get_station_by_id**
> StationSet get_station_by_id(station_id)

Find a Station by station_id

Devices all belong to a Station.  This response contains Station metadata and metadata for the Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a time.  Only devices with a serial_number value can send new observations.  A Device wihout a serial_number indicates that Device is no longer active.

### Example

* Api Key Authentication (swdApiKey):
* OAuth Authentication (swdImplicit):
```python
import time
import os
import weatherflow_openapi
from weatherflow_openapi.models.station_set import StationSet
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
    api_instance = weatherflow_openapi.StationsApi(api_client)
    station_id = 56 # int | ID of Station to return

    try:
        # Find a Station by station_id
        api_response = await api_instance.get_station_by_id(station_id)
        print("The response of StationsApi->get_station_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StationsApi->get_station_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **int**| ID of Station to return | 

### Return type

[**StationSet**](StationSet.md)

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

# **get_stations**
> StationSet get_stations()

Find all Stations for a user

Devices all belong to a Station.  This response contains Station metadata and metadata for the Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a time.  Only devices with a serial_number value can send new observations.  A Device wihout a serial_number indicates that Device is no longer active.

### Example

* Api Key Authentication (swdApiKey):
* OAuth Authentication (swdImplicit):
```python
import time
import os
import weatherflow_openapi
from weatherflow_openapi.models.station_set import StationSet
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
    api_instance = weatherflow_openapi.StationsApi(api_client)

    try:
        # Find all Stations for a user
        api_response = await api_instance.get_stations()
        print("The response of StationsApi->get_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StationsApi->get_stations: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**StationSet**](StationSet.md)

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

