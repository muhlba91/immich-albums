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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from openapi_client.models.system_config_f_fmpeg_dto import SystemConfigFFmpegDto
from openapi_client.models.system_config_image_dto import SystemConfigImageDto
from openapi_client.models.system_config_job_dto import SystemConfigJobDto
from openapi_client.models.system_config_library_dto import SystemConfigLibraryDto
from openapi_client.models.system_config_logging_dto import SystemConfigLoggingDto
from openapi_client.models.system_config_machine_learning_dto import SystemConfigMachineLearningDto
from openapi_client.models.system_config_map_dto import SystemConfigMapDto
from openapi_client.models.system_config_new_version_check_dto import SystemConfigNewVersionCheckDto
from openapi_client.models.system_config_o_auth_dto import SystemConfigOAuthDto
from openapi_client.models.system_config_password_login_dto import SystemConfigPasswordLoginDto
from openapi_client.models.system_config_reverse_geocoding_dto import SystemConfigReverseGeocodingDto
from openapi_client.models.system_config_server_dto import SystemConfigServerDto
from openapi_client.models.system_config_storage_template_dto import SystemConfigStorageTemplateDto
from openapi_client.models.system_config_theme_dto import SystemConfigThemeDto
from openapi_client.models.system_config_trash_dto import SystemConfigTrashDto
from openapi_client.models.system_config_user_dto import SystemConfigUserDto
from typing import Optional, Set
from typing_extensions import Self

class SystemConfigDto(BaseModel):
    """
    SystemConfigDto
    """ # noqa: E501
    ffmpeg: SystemConfigFFmpegDto
    image: SystemConfigImageDto
    job: SystemConfigJobDto
    library: SystemConfigLibraryDto
    logging: SystemConfigLoggingDto
    machine_learning: SystemConfigMachineLearningDto = Field(alias="machineLearning")
    map: SystemConfigMapDto
    new_version_check: SystemConfigNewVersionCheckDto = Field(alias="newVersionCheck")
    oauth: SystemConfigOAuthDto
    password_login: SystemConfigPasswordLoginDto = Field(alias="passwordLogin")
    reverse_geocoding: SystemConfigReverseGeocodingDto = Field(alias="reverseGeocoding")
    server: SystemConfigServerDto
    storage_template: SystemConfigStorageTemplateDto = Field(alias="storageTemplate")
    theme: SystemConfigThemeDto
    trash: SystemConfigTrashDto
    user: SystemConfigUserDto
    __properties: ClassVar[List[str]] = ["ffmpeg", "image", "job", "library", "logging", "machineLearning", "map", "newVersionCheck", "oauth", "passwordLogin", "reverseGeocoding", "server", "storageTemplate", "theme", "trash", "user"]

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
        """Create an instance of SystemConfigDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ffmpeg
        if self.ffmpeg:
            _dict['ffmpeg'] = self.ffmpeg.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job
        if self.job:
            _dict['job'] = self.job.to_dict()
        # override the default output from pydantic by calling `to_dict()` of library
        if self.library:
            _dict['library'] = self.library.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logging
        if self.logging:
            _dict['logging'] = self.logging.to_dict()
        # override the default output from pydantic by calling `to_dict()` of machine_learning
        if self.machine_learning:
            _dict['machineLearning'] = self.machine_learning.to_dict()
        # override the default output from pydantic by calling `to_dict()` of map
        if self.map:
            _dict['map'] = self.map.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_version_check
        if self.new_version_check:
            _dict['newVersionCheck'] = self.new_version_check.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oauth
        if self.oauth:
            _dict['oauth'] = self.oauth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of password_login
        if self.password_login:
            _dict['passwordLogin'] = self.password_login.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reverse_geocoding
        if self.reverse_geocoding:
            _dict['reverseGeocoding'] = self.reverse_geocoding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict['server'] = self.server.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_template
        if self.storage_template:
            _dict['storageTemplate'] = self.storage_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of theme
        if self.theme:
            _dict['theme'] = self.theme.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trash
        if self.trash:
            _dict['trash'] = self.trash.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemConfigDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ffmpeg": SystemConfigFFmpegDto.from_dict(obj["ffmpeg"]) if obj.get("ffmpeg") is not None else None,
            "image": SystemConfigImageDto.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "job": SystemConfigJobDto.from_dict(obj["job"]) if obj.get("job") is not None else None,
            "library": SystemConfigLibraryDto.from_dict(obj["library"]) if obj.get("library") is not None else None,
            "logging": SystemConfigLoggingDto.from_dict(obj["logging"]) if obj.get("logging") is not None else None,
            "machineLearning": SystemConfigMachineLearningDto.from_dict(obj["machineLearning"]) if obj.get("machineLearning") is not None else None,
            "map": SystemConfigMapDto.from_dict(obj["map"]) if obj.get("map") is not None else None,
            "newVersionCheck": SystemConfigNewVersionCheckDto.from_dict(obj["newVersionCheck"]) if obj.get("newVersionCheck") is not None else None,
            "oauth": SystemConfigOAuthDto.from_dict(obj["oauth"]) if obj.get("oauth") is not None else None,
            "passwordLogin": SystemConfigPasswordLoginDto.from_dict(obj["passwordLogin"]) if obj.get("passwordLogin") is not None else None,
            "reverseGeocoding": SystemConfigReverseGeocodingDto.from_dict(obj["reverseGeocoding"]) if obj.get("reverseGeocoding") is not None else None,
            "server": SystemConfigServerDto.from_dict(obj["server"]) if obj.get("server") is not None else None,
            "storageTemplate": SystemConfigStorageTemplateDto.from_dict(obj["storageTemplate"]) if obj.get("storageTemplate") is not None else None,
            "theme": SystemConfigThemeDto.from_dict(obj["theme"]) if obj.get("theme") is not None else None,
            "trash": SystemConfigTrashDto.from_dict(obj["trash"]) if obj.get("trash") is not None else None,
            "user": SystemConfigUserDto.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


