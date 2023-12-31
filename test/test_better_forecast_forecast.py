# coding: utf-8

"""
    WeatherFlow Tempest API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: jforare@weatherflow.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from weatherflow_openapi.models.better_forecast_forecast import BetterForecastForecast  # noqa: E501

class TestBetterForecastForecast(unittest.TestCase):
    """BetterForecastForecast unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BetterForecastForecast:
        """Test BetterForecastForecast
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BetterForecastForecast`
        """
        model = BetterForecastForecast()  # noqa: E501
        if include_optional:
            return BetterForecastForecast(
                daily = [
                    weatherflow_openapi.models.better_forecast_daily_forecast.BetterForecastDailyForecast(
                        day_start_local = 1.6086996E+9, 
                        day_num = 23.0, 
                        month_num = 12.0, 
                        conditions = 'Clear', 
                        icon = 'clear-day', 
                        sunrise = 1608639322, 
                        sunset = 1608676362, 
                        air_temp_high = 73.0, 
                        air_temp_low = 39.0, 
                        precip_probability = 10.0, 
                        precip_icon = 'chance-rain', 
                        precip_type = 'rain', )
                    ],
                hourly = [
                    weatherflow_openapi.models.better_forecast_hourly_forecast.BetterForecastHourlyForecast(
                        time = 1.6087356E+9, 
                        conditions = 'Clear', 
                        icon = 'clear-day', 
                        air_temperature = 57.0, 
                        sea_level_pressure = 30.257, 
                        relative_humidity = 82.0, 
                        precip = 0.0, 
                        precip_probability = 0.0, 
                        wind_avg = 2.0, 
                        wind_direction = 34.0, 
                        wind_direction_cardinal = 'NE', 
                        wind_gust = 3.0, 
                        uv = 2.0, 
                        feels_like = 57.0, 
                        local_hour = 10.0, 
                        local_day = 23.0, )
                    ]
            )
        else:
            return BetterForecastForecast(
        )
        """

    def testBetterForecastForecast(self):
        """Test BetterForecastForecast"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
