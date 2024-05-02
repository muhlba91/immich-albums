# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.103.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.asset_type_enum import AssetTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class SmartSearchDto(BaseModel):
    """
    SmartSearchDto
    """ # noqa: E501
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    created_after: Optional[datetime] = Field(default=None, alias="createdAfter")
    created_before: Optional[datetime] = Field(default=None, alias="createdBefore")
    device_id: Optional[StrictStr] = Field(default=None, alias="deviceId")
    is_archived: Optional[StrictBool] = Field(default=None, alias="isArchived")
    is_encoded: Optional[StrictBool] = Field(default=None, alias="isEncoded")
    is_external: Optional[StrictBool] = Field(default=None, alias="isExternal")
    is_favorite: Optional[StrictBool] = Field(default=None, alias="isFavorite")
    is_motion: Optional[StrictBool] = Field(default=None, alias="isMotion")
    is_not_in_album: Optional[StrictBool] = Field(default=None, alias="isNotInAlbum")
    is_offline: Optional[StrictBool] = Field(default=None, alias="isOffline")
    is_read_only: Optional[StrictBool] = Field(default=None, alias="isReadOnly")
    is_visible: Optional[StrictBool] = Field(default=None, alias="isVisible")
    lens_model: Optional[StrictStr] = Field(default=None, alias="lensModel")
    library_id: Optional[StrictStr] = Field(default=None, alias="libraryId")
    make: Optional[StrictStr] = None
    model: Optional[StrictStr] = None
    page: Optional[Union[Annotated[float, Field(strict=True, ge=1)], Annotated[int, Field(strict=True, ge=1)]]] = None
    person_ids: Optional[List[StrictStr]] = Field(default=None, alias="personIds")
    query: StrictStr
    size: Optional[Union[Annotated[float, Field(le=1000, strict=True, ge=1)], Annotated[int, Field(le=1000, strict=True, ge=1)]]] = None
    state: Optional[StrictStr] = None
    taken_after: Optional[datetime] = Field(default=None, alias="takenAfter")
    taken_before: Optional[datetime] = Field(default=None, alias="takenBefore")
    trashed_after: Optional[datetime] = Field(default=None, alias="trashedAfter")
    trashed_before: Optional[datetime] = Field(default=None, alias="trashedBefore")
    type: Optional[AssetTypeEnum] = None
    updated_after: Optional[datetime] = Field(default=None, alias="updatedAfter")
    updated_before: Optional[datetime] = Field(default=None, alias="updatedBefore")
    with_archived: Optional[StrictBool] = Field(default=False, alias="withArchived")
    with_deleted: Optional[StrictBool] = Field(default=None, alias="withDeleted")
    with_exif: Optional[StrictBool] = Field(default=None, alias="withExif")
    __properties: ClassVar[List[str]] = ["city", "country", "createdAfter", "createdBefore", "deviceId", "isArchived", "isEncoded", "isExternal", "isFavorite", "isMotion", "isNotInAlbum", "isOffline", "isReadOnly", "isVisible", "lensModel", "libraryId", "make", "model", "page", "personIds", "query", "size", "state", "takenAfter", "takenBefore", "trashedAfter", "trashedBefore", "type", "updatedAfter", "updatedBefore", "withArchived", "withDeleted", "withExif"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SmartSearchDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmartSearchDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "city": obj.get("city"),
            "country": obj.get("country"),
            "createdAfter": obj.get("createdAfter"),
            "createdBefore": obj.get("createdBefore"),
            "deviceId": obj.get("deviceId"),
            "isArchived": obj.get("isArchived"),
            "isEncoded": obj.get("isEncoded"),
            "isExternal": obj.get("isExternal"),
            "isFavorite": obj.get("isFavorite"),
            "isMotion": obj.get("isMotion"),
            "isNotInAlbum": obj.get("isNotInAlbum"),
            "isOffline": obj.get("isOffline"),
            "isReadOnly": obj.get("isReadOnly"),
            "isVisible": obj.get("isVisible"),
            "lensModel": obj.get("lensModel"),
            "libraryId": obj.get("libraryId"),
            "make": obj.get("make"),
            "model": obj.get("model"),
            "page": obj.get("page"),
            "personIds": obj.get("personIds"),
            "query": obj.get("query"),
            "size": obj.get("size"),
            "state": obj.get("state"),
            "takenAfter": obj.get("takenAfter"),
            "takenBefore": obj.get("takenBefore"),
            "trashedAfter": obj.get("trashedAfter"),
            "trashedBefore": obj.get("trashedBefore"),
            "type": obj.get("type"),
            "updatedAfter": obj.get("updatedAfter"),
            "updatedBefore": obj.get("updatedBefore"),
            "withArchived": obj.get("withArchived") if obj.get("withArchived") is not None else False,
            "withDeleted": obj.get("withDeleted"),
            "withExif": obj.get("withExif")
        })
        return _obj


