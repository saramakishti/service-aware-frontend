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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class Eventmessage(BaseModel):
    """
    Eventmessage
    """
    timestamp: StrictInt = Field(...)
    group: StrictInt = Field(...)
    group_id: StrictInt = Field(...)
    msg_type: StrictInt = Field(...)
    src_did: StrictStr = Field(...)
    des_did: StrictStr = Field(...)
    msg: Dict[str, Any] = Field(...)
    id: StrictInt = Field(...)
    __properties = ["timestamp", "group", "group_id", "msg_type", "src_did", "des_did", "msg", "id"]

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
    def from_json(cls, json_str: str) -> Eventmessage:
        """Create an instance of Eventmessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Eventmessage:
        """Create an instance of Eventmessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Eventmessage.parse_obj(obj)

        _obj = Eventmessage.parse_obj({
            "timestamp": obj.get("timestamp"),
            "group": obj.get("group"),
            "group_id": obj.get("group_id"),
            "msg_type": obj.get("msg_type"),
            "src_did": obj.get("src_did"),
            "des_did": obj.get("des_did"),
            "msg": obj.get("msg"),
            "id": obj.get("id")
        })
        return _obj


