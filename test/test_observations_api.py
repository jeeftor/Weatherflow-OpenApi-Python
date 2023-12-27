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

from weatherflow_openapi.api.observations_api import ObservationsApi  # noqa: E501


class TestObservationsApi(unittest.TestCase):
    """ObservationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObservationsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_observations_by_device_id(self) -> None:
        """Test case for get_observations_by_device_id

        Get Observations for a Single Device  # noqa: E501
        """
        pass

    def test_get_station_observation(self) -> None:
        """Test case for get_station_observation

        Get the latest Station observation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
