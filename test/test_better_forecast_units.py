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

from weatherflow_openapi.models.better_forecast_units import BetterForecastUnits  # noqa: E501

class TestBetterForecastUnits(unittest.TestCase):
    """BetterForecastUnits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BetterForecastUnits:
        """Test BetterForecastUnits
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BetterForecastUnits`
        """
        model = BetterForecastUnits()  # noqa: E501
        if include_optional:
            return BetterForecastUnits(
                units_temp = 'f',
                units_wind = 'mph',
                units_precip = 'in',
                units_pressure = 'inhg',
                units_distance = 'mi',
                units_brightness = 'lux',
                units_solar_radiation = 'w/m2',
                units_other = 'imperial',
                units_air_density = 'lbs/ft3'
            )
        else:
            return BetterForecastUnits(
        )
        """

    def testBetterForecastUnits(self):
        """Test BetterForecastUnits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()