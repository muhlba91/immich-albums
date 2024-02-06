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

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto

class PersonWithFacesResponseDto(BaseModel):
    """
    PersonWithFacesResponseDto
    """
    birth_date: Optional[date] = Field(..., alias="birthDate")
    faces: conlist(AssetFaceWithoutPersonResponseDto) = Field(...)
    id: StrictStr = Field(...)
    is_hidden: StrictBool = Field(..., alias="isHidden")
    name: StrictStr = Field(...)
    thumbnail_path: StrictStr = Field(..., alias="thumbnailPath")
    __properties = ["birthDate", "faces", "id", "isHidden", "name", "thumbnailPath"]

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
    def from_json(cls, json_str: str) -> PersonWithFacesResponseDto:
        """Create an instance of PersonWithFacesResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in faces (list)
        _items = []
        if self.faces:
            for _item in self.faces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['faces'] = _items
        # set to None if birth_date (nullable) is None
        # and __fields_set__ contains the field
        if self.birth_date is None and "birth_date" in self.__fields_set__:
            _dict['birthDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonWithFacesResponseDto:
        """Create an instance of PersonWithFacesResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PersonWithFacesResponseDto.parse_obj(obj)

        _obj = PersonWithFacesResponseDto.parse_obj({
            "birth_date": obj.get("birthDate"),
            "faces": [AssetFaceWithoutPersonResponseDto.from_dict(_item) for _item in obj.get("faces")] if obj.get("faces") is not None else None,
            "id": obj.get("id"),
            "is_hidden": obj.get("isHidden"),
            "name": obj.get("name"),
            "thumbnail_path": obj.get("thumbnailPath")
        })
        return _obj


