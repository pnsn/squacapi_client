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

from squacapi_client.configuration import Configuration


class WriteOnlyNotificationSerializer(object):
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
        'notification_type': 'str',
        'contact': 'int',
        'level': 'int'
    }

    attribute_map = {
        'notification_type': 'notification_type',
        'contact': 'contact',
        'level': 'level'
    }

    def __init__(self, notification_type=None, contact=None, level=None, _configuration=None):  # noqa: E501
        """WriteOnlyNotificationSerializer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._notification_type = None
        self._contact = None
        self._level = None
        self.discriminator = None

        if notification_type is not None:
            self.notification_type = notification_type
        self.contact = contact
        if level is not None:
            self.level = level

    @property
    def notification_type(self):
        """Gets the notification_type of this WriteOnlyNotificationSerializer.  # noqa: E501


        :return: The notification_type of this WriteOnlyNotificationSerializer.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this WriteOnlyNotificationSerializer.


        :param notification_type: The notification_type of this WriteOnlyNotificationSerializer.  # noqa: E501
        :type: str
        """
        allowed_values = ["email", "sms", "slack"]  # noqa: E501
        if (self._configuration.client_side_validation and
                notification_type not in allowed_values):
            raise ValueError(
                "Invalid value for `notification_type` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_type, allowed_values)
            )

        self._notification_type = notification_type

    @property
    def contact(self):
        """Gets the contact of this WriteOnlyNotificationSerializer.  # noqa: E501


        :return: The contact of this WriteOnlyNotificationSerializer.  # noqa: E501
        :rtype: int
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this WriteOnlyNotificationSerializer.


        :param contact: The contact of this WriteOnlyNotificationSerializer.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and contact is None:
            raise ValueError("Invalid value for `contact`, must not be `None`")  # noqa: E501

        self._contact = contact

    @property
    def level(self):
        """Gets the level of this WriteOnlyNotificationSerializer.  # noqa: E501


        :return: The level of this WriteOnlyNotificationSerializer.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this WriteOnlyNotificationSerializer.


        :param level: The level of this WriteOnlyNotificationSerializer.  # noqa: E501
        :type: int
        """

        self._level = level

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
        if issubclass(WriteOnlyNotificationSerializer, dict):
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
        if not isinstance(other, WriteOnlyNotificationSerializer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WriteOnlyNotificationSerializer):
            return True

        return self.to_dict() != other.to_dict()