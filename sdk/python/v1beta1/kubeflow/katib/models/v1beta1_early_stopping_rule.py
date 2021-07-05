# coding: utf-8

"""
    Katib

    Swagger description for Katib  # noqa: E501

    The version of the OpenAPI document: v1beta1-0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.katib.configuration import Configuration


class V1beta1EarlyStoppingRule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'comparison': 'str',
        'name': 'str',
        'start_step': 'int',
        'value': 'str'
    }

    attribute_map = {
        'comparison': 'comparison',
        'name': 'name',
        'start_step': 'startStep',
        'value': 'value'
    }

    def __init__(self, comparison=None, name=None, start_step=None, value=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1EarlyStoppingRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comparison = None
        self._name = None
        self._start_step = None
        self._value = None
        self.discriminator = None

        if comparison is not None:
            self.comparison = comparison
        if name is not None:
            self.name = name
        if start_step is not None:
            self.start_step = start_step
        if value is not None:
            self.value = value

    @property
    def comparison(self):
        """Gets the comparison of this V1beta1EarlyStoppingRule.  # noqa: E501

        Comparison defines correlation between name and value.  # noqa: E501

        :return: The comparison of this V1beta1EarlyStoppingRule.  # noqa: E501
        :rtype: str
        """
        return self._comparison

    @comparison.setter
    def comparison(self, comparison):
        """Sets the comparison of this V1beta1EarlyStoppingRule.

        Comparison defines correlation between name and value.  # noqa: E501

        :param comparison: The comparison of this V1beta1EarlyStoppingRule.  # noqa: E501
        :type: str
        """

        self._comparison = comparison

    @property
    def name(self):
        """Gets the name of this V1beta1EarlyStoppingRule.  # noqa: E501

        Name contains metric name for the rule.  # noqa: E501

        :return: The name of this V1beta1EarlyStoppingRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1EarlyStoppingRule.

        Name contains metric name for the rule.  # noqa: E501

        :param name: The name of this V1beta1EarlyStoppingRule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start_step(self):
        """Gets the start_step of this V1beta1EarlyStoppingRule.  # noqa: E501

        StartStep defines quantity of intermediate results that should be received before applying the rule. If start step is empty, rule is applied from the first recorded metric.  # noqa: E501

        :return: The start_step of this V1beta1EarlyStoppingRule.  # noqa: E501
        :rtype: int
        """
        return self._start_step

    @start_step.setter
    def start_step(self, start_step):
        """Sets the start_step of this V1beta1EarlyStoppingRule.

        StartStep defines quantity of intermediate results that should be received before applying the rule. If start step is empty, rule is applied from the first recorded metric.  # noqa: E501

        :param start_step: The start_step of this V1beta1EarlyStoppingRule.  # noqa: E501
        :type: int
        """

        self._start_step = start_step

    @property
    def value(self):
        """Gets the value of this V1beta1EarlyStoppingRule.  # noqa: E501

        Value contains metric value for the rule.  # noqa: E501

        :return: The value of this V1beta1EarlyStoppingRule.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1beta1EarlyStoppingRule.

        Value contains metric value for the rule.  # noqa: E501

        :param value: The value of this V1beta1EarlyStoppingRule.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1EarlyStoppingRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1EarlyStoppingRule):
            return True

        return self.to_dict() != other.to_dict()
