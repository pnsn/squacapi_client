"""
    Squac API

    API for accessing squac data  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@snippets.local
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "squacapi_client"
VERSION = "2.1.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Squac API",
    author="OpenAPI Generator community",
    author_email="contact@snippets.local",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Squac API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="BSD License",
    long_description="""\
    API for accessing squac data  # noqa: E501
    """
)
