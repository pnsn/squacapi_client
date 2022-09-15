# coding: utf-8

"""
    Squac API

    API for accessing squac data  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReadOnlyGroupDetailSerializer(object):
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
        'name': 'str',
        'id': 'int',
        'description': 'str',
        'channels': 'list[Channel]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'user': 'str',
        'organization': 'int',
        'auto_include_channels': 'list[Channel]',
        'auto_exclude_channels': 'list[Channel]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'channels': 'channels',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user': 'user',
        'organization': 'organization',
        'auto_include_channels': 'auto_include_channels',
        'auto_exclude_channels': 'auto_exclude_channels'
    }

    def __init__(self, name=None, id=None, description=None, channels=None, created_at=None, updated_at=None, user=None, organization=None, auto_include_channels=None, auto_exclude_channels=None):  # noqa: E501
        """ReadOnlyGroupDetailSerializer - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._description = None
        self._channels = None
        self._created_at = None
        self._updated_at = None
        self._user = None
        self._organization = None
        self._auto_include_channels = None
        self._auto_exclude_channels = None
        self.discriminator = None
        self.name = name
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if channels is not None:
            self.channels = channels
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user
        self.organization = organization
        if auto_include_channels is not None:
            self.auto_include_channels = auto_include_channels
        if auto_exclude_channels is not None:
            self.auto_exclude_channels = auto_exclude_channels

    @property
    def name(self):
        """Gets the name of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The name of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReadOnlyGroupDetailSerializer.


        :param name: The name of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The id of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReadOnlyGroupDetailSerializer.


        :param id: The id of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The description of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReadOnlyGroupDetailSerializer.


        :param description: The description of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def channels(self):
        """Gets the channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: list[Channel]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this ReadOnlyGroupDetailSerializer.


        :param channels: The channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: list[Channel]
        """

        self._channels = channels

    @property
    def created_at(self):
        """Gets the created_at of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The created_at of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReadOnlyGroupDetailSerializer.


        :param created_at: The created_at of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The updated_at of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ReadOnlyGroupDetailSerializer.


        :param updated_at: The updated_at of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The user of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ReadOnlyGroupDetailSerializer.


        :param user: The user of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def organization(self):
        """Gets the organization of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The organization of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: int
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ReadOnlyGroupDetailSerializer.


        :param organization: The organization of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: int
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def auto_include_channels(self):
        """Gets the auto_include_channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The auto_include_channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: list[Channel]
        """
        return self._auto_include_channels

    @auto_include_channels.setter
    def auto_include_channels(self, auto_include_channels):
        """Sets the auto_include_channels of this ReadOnlyGroupDetailSerializer.


        :param auto_include_channels: The auto_include_channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: list[Channel]
        """

        self._auto_include_channels = auto_include_channels

    @property
    def auto_exclude_channels(self):
        """Gets the auto_exclude_channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501


        :return: The auto_exclude_channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :rtype: list[Channel]
        """
        return self._auto_exclude_channels

    @auto_exclude_channels.setter
    def auto_exclude_channels(self, auto_exclude_channels):
        """Sets the auto_exclude_channels of this ReadOnlyGroupDetailSerializer.


        :param auto_exclude_channels: The auto_exclude_channels of this ReadOnlyGroupDetailSerializer.  # noqa: E501
        :type: list[Channel]
        """

        self._auto_exclude_channels = auto_exclude_channels

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
        if issubclass(ReadOnlyGroupDetailSerializer, dict):
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
        if not isinstance(other, ReadOnlyGroupDetailSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
