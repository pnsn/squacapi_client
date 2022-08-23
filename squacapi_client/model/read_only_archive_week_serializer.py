"""
    Squac API

    API for accessing squac data  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@snippets.local
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from squacapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from squacapi_client.exceptions import ApiAttributeError



class ReadOnlyArchiveWeekSerializer(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('num_samps',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'channel': (int,),  # noqa: E501
            'metric': (int,),  # noqa: E501
            'min': (float,),  # noqa: E501
            'max': (float,),  # noqa: E501
            'mean': (float,),  # noqa: E501
            'median': (float,),  # noqa: E501
            'stdev': (float,),  # noqa: E501
            'num_samps': (int,),  # noqa: E501
            'p05': (float,),  # noqa: E501
            'p10': (float,),  # noqa: E501
            'p90': (float,),  # noqa: E501
            'p95': (float,),  # noqa: E501
            'starttime': (datetime,),  # noqa: E501
            'endtime': (datetime,),  # noqa: E501
            'minabs': (str,),  # noqa: E501
            'maxabs': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'channel': 'channel',  # noqa: E501
        'metric': 'metric',  # noqa: E501
        'min': 'min',  # noqa: E501
        'max': 'max',  # noqa: E501
        'mean': 'mean',  # noqa: E501
        'median': 'median',  # noqa: E501
        'stdev': 'stdev',  # noqa: E501
        'num_samps': 'num_samps',  # noqa: E501
        'p05': 'p05',  # noqa: E501
        'p10': 'p10',  # noqa: E501
        'p90': 'p90',  # noqa: E501
        'p95': 'p95',  # noqa: E501
        'starttime': 'starttime',  # noqa: E501
        'endtime': 'endtime',  # noqa: E501
        'minabs': 'minabs',  # noqa: E501
        'maxabs': 'maxabs',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
    }

    read_only_vars = {
        'minabs',  # noqa: E501
        'maxabs',  # noqa: E501
        'id',  # noqa: E501
        'created_at',  # noqa: E501
        'updated_at',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, channel, metric, min, max, mean, median, stdev, num_samps, p05, p10, p90, p95, starttime, endtime, *args, **kwargs):  # noqa: E501
        """ReadOnlyArchiveWeekSerializer - a model defined in OpenAPI

        Args:
            channel (int):
            metric (int):
            min (float):
            max (float):
            mean (float):
            median (float):
            stdev (float):
            num_samps (int):
            p05 (float):
            p10 (float):
            p90 (float):
            p95 (float):
            starttime (datetime):
            endtime (datetime):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            minabs (str): [optional]  # noqa: E501
            maxabs (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.channel = channel
        self.metric = metric
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
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, channel, metric, min, max, mean, median, stdev, num_samps, p05, p10, p90, p95, starttime, endtime, *args, **kwargs):  # noqa: E501
        """ReadOnlyArchiveWeekSerializer - a model defined in OpenAPI

        Args:
            channel (int):
            metric (int):
            min (float):
            max (float):
            mean (float):
            median (float):
            stdev (float):
            num_samps (int):
            p05 (float):
            p10 (float):
            p90 (float):
            p95 (float):
            starttime (datetime):
            endtime (datetime):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            minabs (str): [optional]  # noqa: E501
            maxabs (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.channel = channel
        self.metric = metric
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
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
