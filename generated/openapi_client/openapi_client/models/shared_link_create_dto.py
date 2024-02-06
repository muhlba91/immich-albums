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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.shared_link_type import SharedLinkType

class SharedLinkCreateDto(BaseModel):
    """
    SharedLinkCreateDto
    """
    album_id: Optional[StrictStr] = Field(None, alias="albumId")
    allow_download: Optional[StrictBool] = Field(True, alias="allowDownload")
    allow_upload: Optional[StrictBool] = Field(False, alias="allowUpload")
    asset_ids: Optional[conlist(StrictStr)] = Field(None, alias="assetIds")
    description: Optional[StrictStr] = None
    expires_at: Optional[datetime] = Field(None, alias="expiresAt")
    password: Optional[StrictStr] = None
    show_metadata: Optional[StrictBool] = Field(True, alias="showMetadata")
    type: SharedLinkType = Field(...)
    __properties = ["albumId", "allowDownload", "allowUpload", "assetIds", "description", "expiresAt", "password", "showMetadata", "type"]

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
    def from_json(cls, json_str: str) -> SharedLinkCreateDto:
        """Create an instance of SharedLinkCreateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if expires_at (nullable) is None
        # and __fields_set__ contains the field
        if self.expires_at is None and "expires_at" in self.__fields_set__:
            _dict['expiresAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SharedLinkCreateDto:
        """Create an instance of SharedLinkCreateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SharedLinkCreateDto.parse_obj(obj)

        _obj = SharedLinkCreateDto.parse_obj({
            "album_id": obj.get("albumId"),
            "allow_download": obj.get("allowDownload") if obj.get("allowDownload") is not None else True,
            "allow_upload": obj.get("allowUpload") if obj.get("allowUpload") is not None else False,
            "asset_ids": obj.get("assetIds"),
            "description": obj.get("description"),
            "expires_at": obj.get("expiresAt"),
            "password": obj.get("password"),
            "show_metadata": obj.get("showMetadata") if obj.get("showMetadata") is not None else True,
            "type": obj.get("type")
        })
        return _obj


