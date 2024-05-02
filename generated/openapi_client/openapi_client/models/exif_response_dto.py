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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ExifResponseDto(BaseModel):
    """
    ExifResponseDto
    """ # noqa: E501
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    date_time_original: Optional[datetime] = Field(default=None, alias="dateTimeOriginal")
    description: Optional[StrictStr] = None
    exif_image_height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="exifImageHeight")
    exif_image_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="exifImageWidth")
    exposure_time: Optional[StrictStr] = Field(default=None, alias="exposureTime")
    f_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fNumber")
    file_size_in_byte: Optional[StrictInt] = Field(default=None, alias="fileSizeInByte")
    focal_length: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="focalLength")
    iso: Optional[Union[StrictFloat, StrictInt]] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    lens_model: Optional[StrictStr] = Field(default=None, alias="lensModel")
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    make: Optional[StrictStr] = None
    model: Optional[StrictStr] = None
    modify_date: Optional[datetime] = Field(default=None, alias="modifyDate")
    orientation: Optional[StrictStr] = None
    projection_type: Optional[StrictStr] = Field(default=None, alias="projectionType")
    state: Optional[StrictStr] = None
    time_zone: Optional[StrictStr] = Field(default=None, alias="timeZone")
    __properties: ClassVar[List[str]] = ["city", "country", "dateTimeOriginal", "description", "exifImageHeight", "exifImageWidth", "exposureTime", "fNumber", "fileSizeInByte", "focalLength", "iso", "latitude", "lensModel", "longitude", "make", "model", "modifyDate", "orientation", "projectionType", "state", "timeZone"]

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
        """Create an instance of ExifResponseDto from a JSON string"""
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
        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if date_time_original (nullable) is None
        # and model_fields_set contains the field
        if self.date_time_original is None and "date_time_original" in self.model_fields_set:
            _dict['dateTimeOriginal'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if exif_image_height (nullable) is None
        # and model_fields_set contains the field
        if self.exif_image_height is None and "exif_image_height" in self.model_fields_set:
            _dict['exifImageHeight'] = None

        # set to None if exif_image_width (nullable) is None
        # and model_fields_set contains the field
        if self.exif_image_width is None and "exif_image_width" in self.model_fields_set:
            _dict['exifImageWidth'] = None

        # set to None if exposure_time (nullable) is None
        # and model_fields_set contains the field
        if self.exposure_time is None and "exposure_time" in self.model_fields_set:
            _dict['exposureTime'] = None

        # set to None if f_number (nullable) is None
        # and model_fields_set contains the field
        if self.f_number is None and "f_number" in self.model_fields_set:
            _dict['fNumber'] = None

        # set to None if file_size_in_byte (nullable) is None
        # and model_fields_set contains the field
        if self.file_size_in_byte is None and "file_size_in_byte" in self.model_fields_set:
            _dict['fileSizeInByte'] = None

        # set to None if focal_length (nullable) is None
        # and model_fields_set contains the field
        if self.focal_length is None and "focal_length" in self.model_fields_set:
            _dict['focalLength'] = None

        # set to None if iso (nullable) is None
        # and model_fields_set contains the field
        if self.iso is None and "iso" in self.model_fields_set:
            _dict['iso'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if lens_model (nullable) is None
        # and model_fields_set contains the field
        if self.lens_model is None and "lens_model" in self.model_fields_set:
            _dict['lensModel'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if make (nullable) is None
        # and model_fields_set contains the field
        if self.make is None and "make" in self.model_fields_set:
            _dict['make'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if modify_date (nullable) is None
        # and model_fields_set contains the field
        if self.modify_date is None and "modify_date" in self.model_fields_set:
            _dict['modifyDate'] = None

        # set to None if orientation (nullable) is None
        # and model_fields_set contains the field
        if self.orientation is None and "orientation" in self.model_fields_set:
            _dict['orientation'] = None

        # set to None if projection_type (nullable) is None
        # and model_fields_set contains the field
        if self.projection_type is None and "projection_type" in self.model_fields_set:
            _dict['projectionType'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if time_zone (nullable) is None
        # and model_fields_set contains the field
        if self.time_zone is None and "time_zone" in self.model_fields_set:
            _dict['timeZone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExifResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "city": obj.get("city"),
            "country": obj.get("country"),
            "dateTimeOriginal": obj.get("dateTimeOriginal"),
            "description": obj.get("description"),
            "exifImageHeight": obj.get("exifImageHeight"),
            "exifImageWidth": obj.get("exifImageWidth"),
            "exposureTime": obj.get("exposureTime"),
            "fNumber": obj.get("fNumber"),
            "fileSizeInByte": obj.get("fileSizeInByte"),
            "focalLength": obj.get("focalLength"),
            "iso": obj.get("iso"),
            "latitude": obj.get("latitude"),
            "lensModel": obj.get("lensModel"),
            "longitude": obj.get("longitude"),
            "make": obj.get("make"),
            "model": obj.get("model"),
            "modifyDate": obj.get("modifyDate"),
            "orientation": obj.get("orientation"),
            "projectionType": obj.get("projectionType"),
            "state": obj.get("state"),
            "timeZone": obj.get("timeZone")
        })
        return _obj


