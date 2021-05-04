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


class WriteOnlyMonitorSerializer(object):
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
        'channel_group': 'int',
        'metric': 'int',
        'interval_type': 'str',
        'interval_count': 'int',
        'num_channels': 'int',
        'stat': 'str',
        'name': 'str'
    }

    attribute_map = {
        'channel_group': 'channel_group',
        'metric': 'metric',
        'interval_type': 'interval_type',
        'interval_count': 'interval_count',
        'num_channels': 'num_channels',
        'stat': 'stat',
        'name': 'name'
    }

    def __init__(self, channel_group=None, metric=None, interval_type=None, interval_count=None, num_channels=None, stat=None, name=None, _configuration=None):  # noqa: E501
        """WriteOnlyMonitorSerializer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._channel_group = None
        self._metric = None
        self._interval_type = None
        self._interval_count = None
        self._num_channels = None
        self._stat = None
        self._name = None
        self.discriminator = None

        self.channel_group = channel_group
        self.metric = metric
        if interval_type is not None:
            self.interval_type = interval_type
        self.interval_count = interval_count
        self.num_channels = num_channels
        if stat is not None:
            self.stat = stat
        if name is not None:
            self.name = name

    @property
    def channel_group(self):
        """Gets the channel_group of this WriteOnlyMonitorSerializer.  # noqa: E501


        :return: The channel_group of this WriteOnlyMonitorSerializer.  # noqa: E501
        :rtype: int
        """
        return self._channel_group

    @channel_group.setter
    def channel_group(self, channel_group):
        """Sets the channel_group of this WriteOnlyMonitorSerializer.


        :param channel_group: The channel_group of this WriteOnlyMonitorSerializer.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and channel_group is None:
            raise ValueError("Invalid value for `channel_group`, must not be `None`")  # noqa: E501

        self._channel_group = channel_group

    @property
    def metric(self):
        """Gets the metric of this WriteOnlyMonitorSerializer.  # noqa: E501


        :return: The metric of this WriteOnlyMonitorSerializer.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this WriteOnlyMonitorSerializer.


        :param metric: The metric of this WriteOnlyMonitorSerializer.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def interval_type(self):
        """Gets the interval_type of this WriteOnlyMonitorSerializer.  # noqa: E501


        :return: The interval_type of this WriteOnlyMonitorSerializer.  # noqa: E501
        :rtype: str
        """
        return self._interval_type

    @interval_type.setter
    def interval_type(self, interval_type):
        """Sets the interval_type of this WriteOnlyMonitorSerializer.


        :param interval_type: The interval_type of this WriteOnlyMonitorSerializer.  # noqa: E501
        :type: str
        """
        allowed_values = ["minute", "hour", "day"]  # noqa: E501
        if (self._configuration.client_side_validation and
                interval_type not in allowed_values):
            raise ValueError(
                "Invalid value for `interval_type` ({0}), must be one of {1}"  # noqa: E501
                .format(interval_type, allowed_values)
            )

        self._interval_type = interval_type

    @property
    def interval_count(self):
        """Gets the interval_count of this WriteOnlyMonitorSerializer.  # noqa: E501


        :return: The interval_count of this WriteOnlyMonitorSerializer.  # noqa: E501
        :rtype: int
        """
        return self._interval_count

    @interval_count.setter
    def interval_count(self, interval_count):
        """Sets the interval_count of this WriteOnlyMonitorSerializer.


        :param interval_count: The interval_count of this WriteOnlyMonitorSerializer.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and interval_count is None:
            raise ValueError("Invalid value for `interval_count`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                interval_count is not None and interval_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `interval_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                interval_count is not None and interval_count < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `interval_count`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._interval_count = interval_count

    @property
    def num_channels(self):
        """Gets the num_channels of this WriteOnlyMonitorSerializer.  # noqa: E501


        :return: The num_channels of this WriteOnlyMonitorSerializer.  # noqa: E501
        :rtype: int
        """
        return self._num_channels

    @num_channels.setter
    def num_channels(self, num_channels):
        """Sets the num_channels of this WriteOnlyMonitorSerializer.


        :param num_channels: The num_channels of this WriteOnlyMonitorSerializer.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and num_channels is None:
            raise ValueError("Invalid value for `num_channels`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                num_channels is not None and num_channels > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `num_channels`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                num_channels is not None and num_channels < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `num_channels`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._num_channels = num_channels

    @property
    def stat(self):
        """Gets the stat of this WriteOnlyMonitorSerializer.  # noqa: E501


        :return: The stat of this WriteOnlyMonitorSerializer.  # noqa: E501
        :rtype: str
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this WriteOnlyMonitorSerializer.


        :param stat: The stat of this WriteOnlyMonitorSerializer.  # noqa: E501
        :type: str
        """
        allowed_values = ["count", "sum", "avg", "min", "max"]  # noqa: E501
        if (self._configuration.client_side_validation and
                stat not in allowed_values):
            raise ValueError(
                "Invalid value for `stat` ({0}), must be one of {1}"  # noqa: E501
                .format(stat, allowed_values)
            )

        self._stat = stat

    @property
    def name(self):
        """Gets the name of this WriteOnlyMonitorSerializer.  # noqa: E501


        :return: The name of this WriteOnlyMonitorSerializer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WriteOnlyMonitorSerializer.


        :param name: The name of this WriteOnlyMonitorSerializer.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

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
        if issubclass(WriteOnlyMonitorSerializer, dict):
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
        if not isinstance(other, WriteOnlyMonitorSerializer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WriteOnlyMonitorSerializer):
            return True

        return self.to_dict() != other.to_dict()
