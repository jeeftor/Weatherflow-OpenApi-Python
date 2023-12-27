# weatherflow_openapi.ForecastApi

All URIs are relative to *http://swd.weatherflow.com/swd/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_better_forecast**](ForecastApi.md#get_better_forecast) | **GET** /better_forecast | Get Better Forecast Data


# **get_better_forecast**
> BetterForecast get_better_forecast(station_id, units_temp=units_temp, units_wind=units_wind, units_pressure=units_pressure, units_precip=units_precip, units_distance=units_distance)

Get Better Forecast Data

The better forecast includes current conditions, daily forecast and hourly forecast.<br><br><b>Possible Condition Strings:</b><br>Clear<br>Rain Likely<br>Rain Possible<br>Snow<br>Snow Possible<br>Wintry Mix Likely<br>Wintry Mix Possible<br>Thunderstorms Likely<br>Thunderstorms Possible<br>Windy<br>Foggy<br>Cloudy<br>Partly Cloudy<br>Very Light Rain<br><br><b>Possible Icon Values:</b><br>clear-day<br>clear-night<br>cloudy<br>foggy<br>partly-cloudy-day<br>partly-cloudy-night<br>possibly-rainy-day<br>possibly-rainy-night<br>possibly-sleet-day<br>possibly-sleet-night<br>possibly-snow-day<br>possibly-snow-night<br>possibly-thunderstorm-day<br>possibly-thunderstorm-night<br>rainy<br>sleet<br>snow<br>thunderstorm<br>windy<br><br><b>Possible Precip Type Values:</b><br>rain<br>snow<br>sleet<br>storm<br><br><b>Possible Precip Icon Values:</b><br>chance-rain<br>chance-snow<br>chance-sleet<br><br><b>Possible Pressure Trend Values:</b><br>falling<br>steady<br>rising<br>unknown<br><br><b>Possible Wind Direction Cardinal Values:</b><br>N<br>NNE<br>NE<br>ENE<br>E<br>ESE<br>SE<br>SSE<br>S<br>SSW<br>SW<br>WSW<br>W<br>WNW<br>NW<br>NNW<br>N

### Example

* Api Key Authentication (swdApiKey):
* OAuth Authentication (swdImplicit):
```python
import time
import os
import weatherflow_openapi
from weatherflow_openapi.models.better_forecast import BetterForecast
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
    api_instance = weatherflow_openapi.ForecastApi(api_client)
    station_id = 56 # int | The station_id to use in the current conditions response object.
    units_temp = 'units_temp_example' # str | default = c (optional)
    units_wind = 'units_wind_example' # str | default = mps (optional)
    units_pressure = 'units_pressure_example' # str | default = mb (optional)
    units_precip = 'units_precip_example' # str | default = mm (optional)
    units_distance = 'units_distance_example' # str | default = km (optional)

    try:
        # Get Better Forecast Data
        api_response = await api_instance.get_better_forecast(station_id, units_temp=units_temp, units_wind=units_wind, units_pressure=units_pressure, units_precip=units_precip, units_distance=units_distance)
        print("The response of ForecastApi->get_better_forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForecastApi->get_better_forecast: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **int**| The station_id to use in the current conditions response object. | 
 **units_temp** | **str**| default &#x3D; c | [optional] 
 **units_wind** | **str**| default &#x3D; mps | [optional] 
 **units_pressure** | **str**| default &#x3D; mb | [optional] 
 **units_precip** | **str**| default &#x3D; mm | [optional] 
 **units_distance** | **str**| default &#x3D; km | [optional] 

### Return type

[**BetterForecast**](BetterForecast.md)

### Authorization

[swdApiKey](../README.md#swdApiKey), [swdImplicit](../README.md#swdImplicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

