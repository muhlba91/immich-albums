# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.94.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.asset_response_dto import AssetResponseDto

class MemoryLaneResponseDto(BaseModel):
    """
    MemoryLaneResponseDto
    """
    assets: conlist(AssetResponseDto) = Field(...)
    title: StrictStr = Field(...)
    __properties = ["assets", "title"]

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
    def from_json(cls, json_str: str) -> MemoryLaneResponseDto:
        """Create an instance of MemoryLaneResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item in self.assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MemoryLaneResponseDto:
        """Create an instance of MemoryLaneResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MemoryLaneResponseDto.parse_obj(obj)

        _obj = MemoryLaneResponseDto.parse_obj({
            "assets": [AssetResponseDto.from_dict(_item) for _item in obj.get("assets")] if obj.get("assets") is not None else None,
            "title": obj.get("title")
        })
        return _obj


