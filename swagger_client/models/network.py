# coding: utf-8

"""
    Squac API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Network(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'class_name': 'str',
        'code': 'str',
        'name': 'str',
        'url': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'user': 'str'
    }

    attribute_map = {
        'class_name': 'class_name',
        'code': 'code',
        'name': 'name',
        'url': 'url',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, class_name=None, code=None, name=None, url=None, description=None, created_at=None, updated_at=None, user=None):  # noqa: E501
        """Network - a model defined in Swagger"""  # noqa: E501

        self._class_name = None
        self._code = None
        self._name = None
        self._url = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if class_name is not None:
            self.class_name = class_name
        self.code = code
        self.name = name
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def class_name(self):
        """Gets the class_name of this Network.  # noqa: E501


        :return: The class_name of this Network.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this Network.


        :param class_name: The class_name of this Network.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def code(self):
        """Gets the code of this Network.  # noqa: E501


        :return: The code of this Network.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Network.


        :param code: The code of this Network.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) > 2:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `2`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def name(self):
        """Gets the name of this Network.  # noqa: E501


        :return: The name of this Network.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Network.


        :param name: The name of this Network.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this Network.  # noqa: E501


        :return: The url of this Network.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Network.


        :param url: The url of this Network.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """Gets the description of this Network.  # noqa: E501


        :return: The description of this Network.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Network.


        :param description: The description of this Network.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Network.  # noqa: E501


        :return: The created_at of this Network.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Network.


        :param created_at: The created_at of this Network.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Network.  # noqa: E501


        :return: The updated_at of this Network.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Network.


        :param updated_at: The updated_at of this Network.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this Network.  # noqa: E501


        :return: The user of this Network.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Network.


        :param user: The user of this Network.  # noqa: E501
        :type: str
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Network, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
