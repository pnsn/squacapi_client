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


class Widget(object):
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
        'name': 'str',
        'dashboard': 'int',
        'widgettype': 'int',
        'description': 'str',
        'metrics': 'list[int]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'stattype': 'int',
        'columns': 'int',
        'rows': 'int',
        'x_position': 'int',
        'y_position': 'int',
        'channel_group': 'int',
        'user': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'dashboard': 'dashboard',
        'widgettype': 'widgettype',
        'description': 'description',
        'metrics': 'metrics',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'stattype': 'stattype',
        'columns': 'columns',
        'rows': 'rows',
        'x_position': 'x_position',
        'y_position': 'y_position',
        'channel_group': 'channel_group',
        'user': 'user'
    }

    def __init__(self, id=None, name=None, dashboard=None, widgettype=None, description=None, metrics=None, created_at=None, updated_at=None, stattype=None, columns=None, rows=None, x_position=None, y_position=None, channel_group=None, user=None):  # noqa: E501
        """Widget - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._dashboard = None
        self._widgettype = None
        self._description = None
        self._metrics = None
        self._created_at = None
        self._updated_at = None
        self._stattype = None
        self._columns = None
        self._rows = None
        self._x_position = None
        self._y_position = None
        self._channel_group = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.dashboard = dashboard
        self.widgettype = widgettype
        if description is not None:
            self.description = description
        self.metrics = metrics
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.stattype = stattype
        self.columns = columns
        self.rows = rows
        self.x_position = x_position
        self.y_position = y_position
        self.channel_group = channel_group
        if user is not None:
            self.user = user

    @property
    def id(self):
        """Gets the id of this Widget.  # noqa: E501


        :return: The id of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Widget.


        :param id: The id of this Widget.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Widget.  # noqa: E501


        :return: The name of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Widget.


        :param name: The name of this Widget.  # noqa: E501
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
    def dashboard(self):
        """Gets the dashboard of this Widget.  # noqa: E501


        :return: The dashboard of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """Sets the dashboard of this Widget.


        :param dashboard: The dashboard of this Widget.  # noqa: E501
        :type: int
        """
        if dashboard is None:
            raise ValueError("Invalid value for `dashboard`, must not be `None`")  # noqa: E501

        self._dashboard = dashboard

    @property
    def widgettype(self):
        """Gets the widgettype of this Widget.  # noqa: E501


        :return: The widgettype of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._widgettype

    @widgettype.setter
    def widgettype(self, widgettype):
        """Sets the widgettype of this Widget.


        :param widgettype: The widgettype of this Widget.  # noqa: E501
        :type: int
        """
        if widgettype is None:
            raise ValueError("Invalid value for `widgettype`, must not be `None`")  # noqa: E501

        self._widgettype = widgettype

    @property
    def description(self):
        """Gets the description of this Widget.  # noqa: E501


        :return: The description of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Widget.


        :param description: The description of this Widget.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def metrics(self):
        """Gets the metrics of this Widget.  # noqa: E501


        :return: The metrics of this Widget.  # noqa: E501
        :rtype: list[int]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this Widget.


        :param metrics: The metrics of this Widget.  # noqa: E501
        :type: list[int]
        """
        if metrics is None:
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def created_at(self):
        """Gets the created_at of this Widget.  # noqa: E501


        :return: The created_at of this Widget.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Widget.


        :param created_at: The created_at of this Widget.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Widget.  # noqa: E501


        :return: The updated_at of this Widget.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Widget.


        :param updated_at: The updated_at of this Widget.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def stattype(self):
        """Gets the stattype of this Widget.  # noqa: E501


        :return: The stattype of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._stattype

    @stattype.setter
    def stattype(self, stattype):
        """Sets the stattype of this Widget.


        :param stattype: The stattype of this Widget.  # noqa: E501
        :type: int
        """
        if stattype is None:
            raise ValueError("Invalid value for `stattype`, must not be `None`")  # noqa: E501

        self._stattype = stattype

    @property
    def columns(self):
        """Gets the columns of this Widget.  # noqa: E501


        :return: The columns of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Widget.


        :param columns: The columns of this Widget.  # noqa: E501
        :type: int
        """
        if columns is None:
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501
        if columns is not None and columns > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `columns`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if columns is not None and columns < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `columns`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._columns = columns

    @property
    def rows(self):
        """Gets the rows of this Widget.  # noqa: E501


        :return: The rows of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this Widget.


        :param rows: The rows of this Widget.  # noqa: E501
        :type: int
        """
        if rows is None:
            raise ValueError("Invalid value for `rows`, must not be `None`")  # noqa: E501
        if rows is not None and rows > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `rows`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if rows is not None and rows < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `rows`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._rows = rows

    @property
    def x_position(self):
        """Gets the x_position of this Widget.  # noqa: E501


        :return: The x_position of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._x_position

    @x_position.setter
    def x_position(self, x_position):
        """Sets the x_position of this Widget.


        :param x_position: The x_position of this Widget.  # noqa: E501
        :type: int
        """
        if x_position is None:
            raise ValueError("Invalid value for `x_position`, must not be `None`")  # noqa: E501
        if x_position is not None and x_position > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `x_position`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if x_position is not None and x_position < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `x_position`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._x_position = x_position

    @property
    def y_position(self):
        """Gets the y_position of this Widget.  # noqa: E501


        :return: The y_position of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._y_position

    @y_position.setter
    def y_position(self, y_position):
        """Sets the y_position of this Widget.


        :param y_position: The y_position of this Widget.  # noqa: E501
        :type: int
        """
        if y_position is None:
            raise ValueError("Invalid value for `y_position`, must not be `None`")  # noqa: E501
        if y_position is not None and y_position > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `y_position`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if y_position is not None and y_position < -2147483648:  # noqa: E501
            raise ValueError("Invalid value for `y_position`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._y_position = y_position

    @property
    def channel_group(self):
        """Gets the channel_group of this Widget.  # noqa: E501


        :return: The channel_group of this Widget.  # noqa: E501
        :rtype: int
        """
        return self._channel_group

    @channel_group.setter
    def channel_group(self, channel_group):
        """Sets the channel_group of this Widget.


        :param channel_group: The channel_group of this Widget.  # noqa: E501
        :type: int
        """
        if channel_group is None:
            raise ValueError("Invalid value for `channel_group`, must not be `None`")  # noqa: E501

        self._channel_group = channel_group

    @property
    def user(self):
        """Gets the user of this Widget.  # noqa: E501


        :return: The user of this Widget.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Widget.


        :param user: The user of this Widget.  # noqa: E501
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
        if issubclass(Widget, dict):
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
        if not isinstance(other, Widget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
