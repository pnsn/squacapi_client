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

class ReadOnlyAlertSerializer(object):
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
        'id': 'int',
        'trigger': 'int',
        'timestamp': 'datetime',
        'message': 'str',
        'in_alarm': 'bool',
        'breaching_channels': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'user': 'int'
    }

    attribute_map = {
        'id': 'id',
        'trigger': 'trigger',
        'timestamp': 'timestamp',
        'message': 'message',
        'in_alarm': 'in_alarm',
        'breaching_channels': 'breaching_channels',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, id=None, trigger=None, timestamp=None, message=None, in_alarm=None, breaching_channels=None, created_at=None, updated_at=None, user=None):  # noqa: E501
        """ReadOnlyAlertSerializer - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._trigger = None
        self._timestamp = None
        self._message = None
        self._in_alarm = None
        self._breaching_channels = None
        self._created_at = None
        self._updated_at = None
        self._user = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.trigger = trigger
        self.timestamp = timestamp
        self.message = message
        if in_alarm is not None:
            self.in_alarm = in_alarm
        if breaching_channels is not None:
            self.breaching_channels = breaching_channels
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def id(self):
        """Gets the id of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The id of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReadOnlyAlertSerializer.


        :param id: The id of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def trigger(self):
        """Gets the trigger of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The trigger of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: int
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this ReadOnlyAlertSerializer.


        :param trigger: The trigger of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: int
        """
        if trigger is None:
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501

        self._trigger = trigger

    @property
    def timestamp(self):
        """Gets the timestamp of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The timestamp of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ReadOnlyAlertSerializer.


        :param timestamp: The timestamp of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def message(self):
        """Gets the message of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The message of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ReadOnlyAlertSerializer.


        :param message: The message of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def in_alarm(self):
        """Gets the in_alarm of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The in_alarm of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: bool
        """
        return self._in_alarm

    @in_alarm.setter
    def in_alarm(self, in_alarm):
        """Sets the in_alarm of this ReadOnlyAlertSerializer.


        :param in_alarm: The in_alarm of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: bool
        """

        self._in_alarm = in_alarm

    @property
    def breaching_channels(self):
        """Gets the breaching_channels of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The breaching_channels of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: str
        """
        return self._breaching_channels

    @breaching_channels.setter
    def breaching_channels(self, breaching_channels):
        """Sets the breaching_channels of this ReadOnlyAlertSerializer.


        :param breaching_channels: The breaching_channels of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: str
        """

        self._breaching_channels = breaching_channels

    @property
    def created_at(self):
        """Gets the created_at of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The created_at of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReadOnlyAlertSerializer.


        :param created_at: The created_at of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The updated_at of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ReadOnlyAlertSerializer.


        :param updated_at: The updated_at of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this ReadOnlyAlertSerializer.  # noqa: E501


        :return: The user of this ReadOnlyAlertSerializer.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ReadOnlyAlertSerializer.


        :param user: The user of this ReadOnlyAlertSerializer.  # noqa: E501
        :type: int
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
        if issubclass(ReadOnlyAlertSerializer, dict):
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
        if not isinstance(other, ReadOnlyAlertSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
