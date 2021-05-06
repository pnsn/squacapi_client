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


class UserSimple(object):
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
        'email': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'id': 'int',
        'is_active': 'bool',
        'last_login': 'datetime',
        'organization': 'int',
        'is_org_admin': 'bool',
        'groups': 'list[int]'
    }

    attribute_map = {
        'email': 'email',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'id': 'id',
        'is_active': 'is_active',
        'last_login': 'last_login',
        'organization': 'organization',
        'is_org_admin': 'is_org_admin',
        'groups': 'groups'
    }

    def __init__(self, email=None, firstname=None, lastname=None, id=None, is_active=None, last_login=None, organization=None, is_org_admin=None, groups=None, _configuration=None):  # noqa: E501
        """UserSimple - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._firstname = None
        self._lastname = None
        self._id = None
        self._is_active = None
        self._last_login = None
        self._organization = None
        self._is_org_admin = None
        self._groups = None
        self.discriminator = None

        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        if id is not None:
            self.id = id
        if is_active is not None:
            self.is_active = is_active
        if last_login is not None:
            self.last_login = last_login
        self.organization = organization
        if is_org_admin is not None:
            self.is_org_admin = is_org_admin
        self.groups = groups

    @property
    def email(self):
        """Gets the email of this UserSimple.  # noqa: E501


        :return: The email of this UserSimple.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserSimple.


        :param email: The email of this UserSimple.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                email is not None and len(email) > 255):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this UserSimple.  # noqa: E501


        :return: The firstname of this UserSimple.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserSimple.


        :param firstname: The firstname of this UserSimple.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                firstname is not None and len(firstname) > 255):
            raise ValueError("Invalid value for `firstname`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                firstname is not None and len(firstname) < 1):
            raise ValueError("Invalid value for `firstname`, length must be greater than or equal to `1`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UserSimple.  # noqa: E501


        :return: The lastname of this UserSimple.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserSimple.


        :param lastname: The lastname of this UserSimple.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                lastname is not None and len(lastname) > 255):
            raise ValueError("Invalid value for `lastname`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                lastname is not None and len(lastname) < 1):
            raise ValueError("Invalid value for `lastname`, length must be greater than or equal to `1`")  # noqa: E501

        self._lastname = lastname

    @property
    def id(self):
        """Gets the id of this UserSimple.  # noqa: E501


        :return: The id of this UserSimple.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSimple.


        :param id: The id of this UserSimple.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_active(self):
        """Gets the is_active of this UserSimple.  # noqa: E501


        :return: The is_active of this UserSimple.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this UserSimple.


        :param is_active: The is_active of this UserSimple.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def last_login(self):
        """Gets the last_login of this UserSimple.  # noqa: E501


        :return: The last_login of this UserSimple.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this UserSimple.


        :param last_login: The last_login of this UserSimple.  # noqa: E501
        :type: datetime
        """

        self._last_login = last_login

    @property
    def organization(self):
        """Gets the organization of this UserSimple.  # noqa: E501


        :return: The organization of this UserSimple.  # noqa: E501
        :rtype: int
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this UserSimple.


        :param organization: The organization of this UserSimple.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def is_org_admin(self):
        """Gets the is_org_admin of this UserSimple.  # noqa: E501


        :return: The is_org_admin of this UserSimple.  # noqa: E501
        :rtype: bool
        """
        return self._is_org_admin

    @is_org_admin.setter
    def is_org_admin(self, is_org_admin):
        """Sets the is_org_admin of this UserSimple.


        :param is_org_admin: The is_org_admin of this UserSimple.  # noqa: E501
        :type: bool
        """

        self._is_org_admin = is_org_admin

    @property
    def groups(self):
        """Gets the groups of this UserSimple.  # noqa: E501


        :return: The groups of this UserSimple.  # noqa: E501
        :rtype: list[int]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserSimple.


        :param groups: The groups of this UserSimple.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

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
        if issubclass(UserSimple, dict):
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
        if not isinstance(other, UserSimple):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSimple):
            return True

        return self.to_dict() != other.to_dict()
