# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict
from pydantic import BaseModel, Field, StrictBool, StrictStr
from openapi_client.models.roles import Roles

class EntityCreate(BaseModel):
    """
    EntityCreate
    """
    did: StrictStr = Field(...)
    name: StrictStr = Field(...)
    ip: StrictStr = Field(...)
    network: StrictStr = Field(...)
    role: Roles = Field(...)
    visible: StrictBool = Field(...)
    other: Dict[str, Any] = Field(...)
    __properties = ["did", "name", "ip", "network", "role", "visible", "other"]

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
    def from_json(cls, json_str: str) -> EntityCreate:
        """Create an instance of EntityCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntityCreate:
        """Create an instance of EntityCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntityCreate.parse_obj(obj)

        _obj = EntityCreate.parse_obj({
            "did": obj.get("did"),
            "name": obj.get("name"),
            "ip": obj.get("ip"),
            "network": obj.get("network"),
            "role": obj.get("role"),
            "visible": obj.get("visible"),
            "other": obj.get("other")
        })
        return _obj


