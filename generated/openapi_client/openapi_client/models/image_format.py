# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.103.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ImageFormat(str, Enum):
    """
    ImageFormat
    """

    """
    allowed enum values
    """
    JPEG = 'jpeg'
    WEBP = 'webp'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ImageFormat from a JSON string"""
        return cls(json.loads(json_str))


