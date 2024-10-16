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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.service_usage import ServiceUsage

class Service(BaseModel):
    """
    Service
    """
    uuid: StrictStr = Field(...)
    service_name: StrictStr = Field(...)
    service_type: StrictStr = Field(...)
    endpoint_url: StrictStr = Field(...)
    other: Dict[str, Any] = Field(...)
    entity_did: StrictStr = Field(...)
    status: Dict[str, Any] = Field(...)
    action: Dict[str, Any] = Field(...)
    usage: conlist(ServiceUsage) = Field(...)
    __properties = ["uuid", "service_name", "service_type", "endpoint_url", "other", "entity_did", "status", "action", "usage"]

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
    def from_json(cls, json_str: str) -> Service:
        """Create an instance of Service from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in usage (list)
        _items = []
        if self.usage:
            for _item in self.usage:
                if _item:
                    _items.append(_item.to_dict())
            _dict['usage'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Service:
        """Create an instance of Service from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Service.parse_obj(obj)

        _obj = Service.parse_obj({
            "uuid": obj.get("uuid"),
            "service_name": obj.get("service_name"),
            "service_type": obj.get("service_type"),
            "endpoint_url": obj.get("endpoint_url"),
            "other": obj.get("other"),
            "entity_did": obj.get("entity_did"),
            "status": obj.get("status"),
            "action": obj.get("action"),
            "usage": [ServiceUsage.from_dict(_item) for _item in obj.get("usage")] if obj.get("usage") is not None else None
        })
        return _obj


