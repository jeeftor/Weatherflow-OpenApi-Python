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

from weatherflow_openapi.models.better_forecast_hourly_forecast import BetterForecastHourlyForecast  # noqa: E501

class TestBetterForecastHourlyForecast(unittest.TestCase):
    """BetterForecastHourlyForecast unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BetterForecastHourlyForecast:
        """Test BetterForecastHourlyForecast
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BetterForecastHourlyForecast`
        """
        model = BetterForecastHourlyForecast()  # noqa: E501
        if include_optional:
            return BetterForecastHourlyForecast(
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
                local_day = 23.0
            )
        else:
            return BetterForecastHourlyForecast(
        )
        """

    def testBetterForecastHourlyForecast(self):
        """Test BetterForecastHourlyForecast"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
