# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.103.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "openapi-client"
VERSION = "1.103.1"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Immich",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Immich"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Immich API
    """,  # noqa: E501
    package_data={"openapi_client": ["py.typed"]},
)
