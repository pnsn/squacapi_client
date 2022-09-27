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

class ReadOnlyArchiveHourSerializer(object):
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
        'channel': 'int',
        'metric': 'int',
        'minabs': 'str',
        'maxabs': 'str',
        'id': 'str',
        'min': 'float',
        'max': 'float',
        'mean': 'float',
        'median': 'float',
        'stdev': 'float',
        'num_samps': 'int',
        'p05': 'float',
        'p10': 'float',
        'p90': 'float',
        'p95': 'float',
        'starttime': 'datetime',
        'endtime': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'channel': 'channel',
        'metric': 'metric',
        'minabs': 'minabs',
        'maxabs': 'maxabs',
        'id': 'id',
        'min': 'min',
        'max': 'max',
        'mean': 'mean',
        'median': 'median',
        'stdev': 'stdev',
        'num_samps': 'num_samps',
        'p05': 'p05',
        'p10': 'p10',
        'p90': 'p90',
        'p95': 'p95',
        'starttime': 'starttime',
        'endtime': 'endtime',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, channel=None, metric=None, minabs=None, maxabs=None, id=None, min=None, max=None, mean=None, median=None, stdev=None, num_samps=None, p05=None, p10=None, p90=None, p95=None, starttime=None, endtime=None, created_at=None, updated_at=None):  # noqa: E501
        """ReadOnlyArchiveHourSerializer - a model defined in Swagger"""  # noqa: E501
        self._channel = None
        self._metric = None
        self._minabs = None
        self._maxabs = None
        self._id = None
        self._min = None
        self._max = None
        self._mean = None
        self._median = None
        self._stdev = None
        self._num_samps = None
        self._p05 = None
        self._p10 = None
        self._p90 = None
        self._p95 = None
        self._starttime = None
        self._endtime = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.channel = channel
        self.metric = metric
        if minabs is not None:
            self.minabs = minabs
        if maxabs is not None:
            self.maxabs = maxabs
        if id is not None:
            self.id = id
        self.min = min
        self.max = max
        self.mean = mean
        self.median = median
        self.stdev = stdev
        self.num_samps = num_samps
        self.p05 = p05
        self.p10 = p10
        self.p90 = p90
        self.p95 = p95
        self.starttime = starttime
        self.endtime = endtime
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def channel(self):
        """Gets the channel of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The channel of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ReadOnlyArchiveHourSerializer.


        :param channel: The channel of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: int
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def metric(self):
        """Gets the metric of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The metric of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ReadOnlyArchiveHourSerializer.


        :param metric: The metric of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: int
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def minabs(self):
        """Gets the minabs of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The minabs of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: str
        """
        return self._minabs

    @minabs.setter
    def minabs(self, minabs):
        """Sets the minabs of this ReadOnlyArchiveHourSerializer.


        :param minabs: The minabs of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: str
        """

        self._minabs = minabs

    @property
    def maxabs(self):
        """Gets the maxabs of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The maxabs of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: str
        """
        return self._maxabs

    @maxabs.setter
    def maxabs(self, maxabs):
        """Sets the maxabs of this ReadOnlyArchiveHourSerializer.


        :param maxabs: The maxabs of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: str
        """

        self._maxabs = maxabs

    @property
    def id(self):
        """Gets the id of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The id of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReadOnlyArchiveHourSerializer.


        :param id: The id of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def min(self):
        """Gets the min of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The min of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ReadOnlyArchiveHourSerializer.


        :param min: The min of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def max(self):
        """Gets the max of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The max of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ReadOnlyArchiveHourSerializer.


        :param max: The max of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def mean(self):
        """Gets the mean of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The mean of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this ReadOnlyArchiveHourSerializer.


        :param mean: The mean of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if mean is None:
            raise ValueError("Invalid value for `mean`, must not be `None`")  # noqa: E501

        self._mean = mean

    @property
    def median(self):
        """Gets the median of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The median of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this ReadOnlyArchiveHourSerializer.


        :param median: The median of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if median is None:
            raise ValueError("Invalid value for `median`, must not be `None`")  # noqa: E501

        self._median = median

    @property
    def stdev(self):
        """Gets the stdev of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The stdev of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._stdev

    @stdev.setter
    def stdev(self, stdev):
        """Sets the stdev of this ReadOnlyArchiveHourSerializer.


        :param stdev: The stdev of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if stdev is None:
            raise ValueError("Invalid value for `stdev`, must not be `None`")  # noqa: E501

        self._stdev = stdev

    @property
    def num_samps(self):
        """Gets the num_samps of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The num_samps of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: int
        """
        return self._num_samps

    @num_samps.setter
    def num_samps(self, num_samps):
        """Sets the num_samps of this ReadOnlyArchiveHourSerializer.


        :param num_samps: The num_samps of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: int
        """
        if num_samps is None:
            raise ValueError("Invalid value for `num_samps`, must not be `None`")  # noqa: E501

        self._num_samps = num_samps

    @property
    def p05(self):
        """Gets the p05 of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The p05 of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._p05

    @p05.setter
    def p05(self, p05):
        """Sets the p05 of this ReadOnlyArchiveHourSerializer.


        :param p05: The p05 of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if p05 is None:
            raise ValueError("Invalid value for `p05`, must not be `None`")  # noqa: E501

        self._p05 = p05

    @property
    def p10(self):
        """Gets the p10 of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The p10 of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._p10

    @p10.setter
    def p10(self, p10):
        """Sets the p10 of this ReadOnlyArchiveHourSerializer.


        :param p10: The p10 of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if p10 is None:
            raise ValueError("Invalid value for `p10`, must not be `None`")  # noqa: E501

        self._p10 = p10

    @property
    def p90(self):
        """Gets the p90 of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The p90 of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._p90

    @p90.setter
    def p90(self, p90):
        """Sets the p90 of this ReadOnlyArchiveHourSerializer.


        :param p90: The p90 of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if p90 is None:
            raise ValueError("Invalid value for `p90`, must not be `None`")  # noqa: E501

        self._p90 = p90

    @property
    def p95(self):
        """Gets the p95 of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The p95 of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: float
        """
        return self._p95

    @p95.setter
    def p95(self, p95):
        """Sets the p95 of this ReadOnlyArchiveHourSerializer.


        :param p95: The p95 of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: float
        """
        if p95 is None:
            raise ValueError("Invalid value for `p95`, must not be `None`")  # noqa: E501

        self._p95 = p95

    @property
    def starttime(self):
        """Gets the starttime of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The starttime of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._starttime

    @starttime.setter
    def starttime(self, starttime):
        """Sets the starttime of this ReadOnlyArchiveHourSerializer.


        :param starttime: The starttime of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: datetime
        """
        if starttime is None:
            raise ValueError("Invalid value for `starttime`, must not be `None`")  # noqa: E501

        self._starttime = starttime

    @property
    def endtime(self):
        """Gets the endtime of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The endtime of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._endtime

    @endtime.setter
    def endtime(self, endtime):
        """Sets the endtime of this ReadOnlyArchiveHourSerializer.


        :param endtime: The endtime of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: datetime
        """
        if endtime is None:
            raise ValueError("Invalid value for `endtime`, must not be `None`")  # noqa: E501

        self._endtime = endtime

    @property
    def created_at(self):
        """Gets the created_at of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The created_at of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReadOnlyArchiveHourSerializer.


        :param created_at: The created_at of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ReadOnlyArchiveHourSerializer.  # noqa: E501


        :return: The updated_at of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ReadOnlyArchiveHourSerializer.


        :param updated_at: The updated_at of this ReadOnlyArchiveHourSerializer.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(ReadOnlyArchiveHourSerializer, dict):
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
        if not isinstance(other, ReadOnlyArchiveHourSerializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
