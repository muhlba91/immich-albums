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


class PathType(str, Enum):
    """
    PathType
    """

    """
    allowed enum values
    """
    ORIGINAL = 'original'
    PREVIEW = 'preview'
    THUMBNAIL = 'thumbnail'
    ENCODED_VIDEO = 'encoded_video'
    SIDECAR = 'sidecar'
    FACE = 'face'
    PROFILE = 'profile'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PathType from a JSON string"""
        return cls(json.loads(json_str))


