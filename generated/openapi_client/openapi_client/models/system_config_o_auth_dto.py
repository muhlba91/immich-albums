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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SystemConfigOAuthDto(BaseModel):
    """
    SystemConfigOAuthDto
    """ # noqa: E501
    auto_launch: StrictBool = Field(alias="autoLaunch")
    auto_register: StrictBool = Field(alias="autoRegister")
    button_text: StrictStr = Field(alias="buttonText")
    client_id: StrictStr = Field(alias="clientId")
    client_secret: StrictStr = Field(alias="clientSecret")
    default_storage_quota: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(alias="defaultStorageQuota")
    enabled: StrictBool
    issuer_url: StrictStr = Field(alias="issuerUrl")
    mobile_override_enabled: StrictBool = Field(alias="mobileOverrideEnabled")
    mobile_redirect_uri: StrictStr = Field(alias="mobileRedirectUri")
    scope: StrictStr
    signing_algorithm: StrictStr = Field(alias="signingAlgorithm")
    storage_label_claim: StrictStr = Field(alias="storageLabelClaim")
    storage_quota_claim: StrictStr = Field(alias="storageQuotaClaim")
    __properties: ClassVar[List[str]] = ["autoLaunch", "autoRegister", "buttonText", "clientId", "clientSecret", "defaultStorageQuota", "enabled", "issuerUrl", "mobileOverrideEnabled", "mobileRedirectUri", "scope", "signingAlgorithm", "storageLabelClaim", "storageQuotaClaim"]

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
        """Create an instance of SystemConfigOAuthDto from a JSON string"""
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
        """Create an instance of SystemConfigOAuthDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "autoLaunch": obj.get("autoLaunch"),
            "autoRegister": obj.get("autoRegister"),
            "buttonText": obj.get("buttonText"),
            "clientId": obj.get("clientId"),
            "clientSecret": obj.get("clientSecret"),
            "defaultStorageQuota": obj.get("defaultStorageQuota"),
            "enabled": obj.get("enabled"),
            "issuerUrl": obj.get("issuerUrl"),
            "mobileOverrideEnabled": obj.get("mobileOverrideEnabled"),
            "mobileRedirectUri": obj.get("mobileRedirectUri"),
            "scope": obj.get("scope"),
            "signingAlgorithm": obj.get("signingAlgorithm"),
            "storageLabelClaim": obj.get("storageLabelClaim"),
            "storageQuotaClaim": obj.get("storageQuotaClaim")
        })
        return _obj


