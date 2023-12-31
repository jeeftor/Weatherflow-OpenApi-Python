# coding: utf-8

"""
    WeatherFlow Tempest API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: jforare@weatherflow.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class BetterForecastHourlyForecast(BaseModel):
    """
    BetterForecastHourlyForecast
    """
    time: Optional[Union[StrictFloat, StrictInt]] = None
    conditions: Optional[StrictStr] = None
    icon: Optional[StrictStr] = None
    air_temperature: Optional[Union[StrictFloat, StrictInt]] = None
    sea_level_pressure: Optional[Union[StrictFloat, StrictInt]] = None
    relative_humidity: Optional[Union[StrictFloat, StrictInt]] = None
    precip: Optional[Union[StrictFloat, StrictInt]] = None
    precip_probability: Optional[Union[StrictFloat, StrictInt]] = None
    wind_avg: Optional[Union[StrictFloat, StrictInt]] = None
    wind_direction: Optional[Union[StrictFloat, StrictInt]] = None
    wind_direction_cardinal: Optional[StrictStr] = None
    wind_gust: Optional[Union[StrictFloat, StrictInt]] = None
    uv: Optional[Union[StrictFloat, StrictInt]] = None
    feels_like: Optional[Union[StrictFloat, StrictInt]] = None
    local_hour: Optional[Union[StrictFloat, StrictInt]] = None
    local_day: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["time", "conditions", "icon", "air_temperature", "sea_level_pressure", "relative_humidity", "precip", "precip_probability", "wind_avg", "wind_direction", "wind_direction_cardinal", "wind_gust", "uv", "feels_like", "local_hour", "local_day"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BetterForecastHourlyForecast:
        """Create an instance of BetterForecastHourlyForecast from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BetterForecastHourlyForecast:
        """Create an instance of BetterForecastHourlyForecast from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BetterForecastHourlyForecast.parse_obj(obj)

        _obj = BetterForecastHourlyForecast.parse_obj({
            "time": obj.get("time"),
            "conditions": obj.get("conditions"),
            "icon": obj.get("icon"),
            "air_temperature": obj.get("air_temperature"),
            "sea_level_pressure": obj.get("sea_level_pressure"),
            "relative_humidity": obj.get("relative_humidity"),
            "precip": obj.get("precip"),
            "precip_probability": obj.get("precip_probability"),
            "wind_avg": obj.get("wind_avg"),
            "wind_direction": obj.get("wind_direction"),
            "wind_direction_cardinal": obj.get("wind_direction_cardinal"),
            "wind_gust": obj.get("wind_gust"),
            "uv": obj.get("uv"),
            "feels_like": obj.get("feels_like"),
            "local_hour": obj.get("local_hour"),
            "local_day": obj.get("local_day")
        })
        return _obj


