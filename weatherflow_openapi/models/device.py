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


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr, validator
from weatherflow_openapi.models.device_meta import DeviceMeta

class Device(BaseModel):
    """
    Device
    """
    device_id: Optional[StrictInt] = None
    serial_number: Optional[StrictStr] = None
    device_meta: Optional[DeviceMeta] = None
    device_type: Optional[StrictStr] = None
    hardware_revision: Optional[StrictStr] = None
    firmware_revision: Optional[StrictStr] = None
    notes: Optional[StrictStr] = None
    __properties = ["device_id", "serial_number", "device_meta", "device_type", "hardware_revision", "firmware_revision", "notes"]

    @validator('device_type')
    def device_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AR', 'SK'):
            raise ValueError("must be one of enum values ('AR', 'SK')")
        return value

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
    def from_json(cls, json_str: str) -> Device:
        """Create an instance of Device from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of device_meta
        if self.device_meta:
            _dict['device_meta'] = self.device_meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Device:
        """Create an instance of Device from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Device.parse_obj(obj)

        _obj = Device.parse_obj({
            "device_id": obj.get("device_id"),
            "serial_number": obj.get("serial_number"),
            "device_meta": DeviceMeta.from_dict(obj.get("device_meta")) if obj.get("device_meta") is not None else None,
            "device_type": obj.get("device_type"),
            "hardware_revision": obj.get("hardware_revision"),
            "firmware_revision": obj.get("firmware_revision"),
            "notes": obj.get("notes")
        })
        return _obj

