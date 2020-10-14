# coding: utf-8

"""
    Katib

    Swagger description for Katib  # noqa: E501

    OpenAPI spec version: v1beta1-0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.katib.models.v1beta1_algorithm_spec import V1beta1AlgorithmSpec  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_early_stopping_spec import V1beta1EarlyStoppingSpec  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_metrics_collector_spec import V1beta1MetricsCollectorSpec  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_nas_config import V1beta1NasConfig  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_objective_spec import V1beta1ObjectiveSpec  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_parameter_spec import V1beta1ParameterSpec  # noqa: F401,E501
from kubeflow.katib.models.v1beta1_trial_template import V1beta1TrialTemplate  # noqa: F401,E501


class V1beta1ExperimentSpec(object):
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
        'algorithm': 'V1beta1AlgorithmSpec',
        'early_stopping': 'V1beta1EarlyStoppingSpec',
        'max_failed_trial_count': 'int',
        'max_trial_count': 'int',
        'metrics_collector_spec': 'V1beta1MetricsCollectorSpec',
        'nas_config': 'V1beta1NasConfig',
        'objective': 'V1beta1ObjectiveSpec',
        'parallel_trial_count': 'int',
        'parameters': 'list[V1beta1ParameterSpec]',
        'resume_policy': 'str',
        'trial_template': 'V1beta1TrialTemplate'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'early_stopping': 'earlyStopping',
        'max_failed_trial_count': 'maxFailedTrialCount',
        'max_trial_count': 'maxTrialCount',
        'metrics_collector_spec': 'metricsCollectorSpec',
        'nas_config': 'nasConfig',
        'objective': 'objective',
        'parallel_trial_count': 'parallelTrialCount',
        'parameters': 'parameters',
        'resume_policy': 'resumePolicy',
        'trial_template': 'trialTemplate'
    }

    def __init__(self, algorithm=None, early_stopping=None, max_failed_trial_count=None, max_trial_count=None, metrics_collector_spec=None, nas_config=None, objective=None, parallel_trial_count=None, parameters=None, resume_policy=None, trial_template=None):  # noqa: E501
        """V1beta1ExperimentSpec - a model defined in Swagger"""  # noqa: E501

        self._algorithm = None
        self._early_stopping = None
        self._max_failed_trial_count = None
        self._max_trial_count = None
        self._metrics_collector_spec = None
        self._nas_config = None
        self._objective = None
        self._parallel_trial_count = None
        self._parameters = None
        self._resume_policy = None
        self._trial_template = None
        self.discriminator = None

        if algorithm is not None:
            self.algorithm = algorithm
        if early_stopping is not None:
            self.early_stopping = early_stopping
        if max_failed_trial_count is not None:
            self.max_failed_trial_count = max_failed_trial_count
        if max_trial_count is not None:
            self.max_trial_count = max_trial_count
        if metrics_collector_spec is not None:
            self.metrics_collector_spec = metrics_collector_spec
        if nas_config is not None:
            self.nas_config = nas_config
        if objective is not None:
            self.objective = objective
        if parallel_trial_count is not None:
            self.parallel_trial_count = parallel_trial_count
        if parameters is not None:
            self.parameters = parameters
        if resume_policy is not None:
            self.resume_policy = resume_policy
        if trial_template is not None:
            self.trial_template = trial_template

    @property
    def algorithm(self):
        """Gets the algorithm of this V1beta1ExperimentSpec.  # noqa: E501

        Describes the suggestion algorithm.  # noqa: E501

        :return: The algorithm of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: V1beta1AlgorithmSpec
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this V1beta1ExperimentSpec.

        Describes the suggestion algorithm.  # noqa: E501

        :param algorithm: The algorithm of this V1beta1ExperimentSpec.  # noqa: E501
        :type: V1beta1AlgorithmSpec
        """

        self._algorithm = algorithm

    @property
    def early_stopping(self):
        """Gets the early_stopping of this V1beta1ExperimentSpec.  # noqa: E501

        Describes the early stopping algorithm.  # noqa: E501

        :return: The early_stopping of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: V1beta1EarlyStoppingSpec
        """
        return self._early_stopping

    @early_stopping.setter
    def early_stopping(self, early_stopping):
        """Sets the early_stopping of this V1beta1ExperimentSpec.

        Describes the early stopping algorithm.  # noqa: E501

        :param early_stopping: The early_stopping of this V1beta1ExperimentSpec.  # noqa: E501
        :type: V1beta1EarlyStoppingSpec
        """

        self._early_stopping = early_stopping

    @property
    def max_failed_trial_count(self):
        """Gets the max_failed_trial_count of this V1beta1ExperimentSpec.  # noqa: E501

        Max failed trials to mark experiment as failed.  # noqa: E501

        :return: The max_failed_trial_count of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_failed_trial_count

    @max_failed_trial_count.setter
    def max_failed_trial_count(self, max_failed_trial_count):
        """Sets the max_failed_trial_count of this V1beta1ExperimentSpec.

        Max failed trials to mark experiment as failed.  # noqa: E501

        :param max_failed_trial_count: The max_failed_trial_count of this V1beta1ExperimentSpec.  # noqa: E501
        :type: int
        """

        self._max_failed_trial_count = max_failed_trial_count

    @property
    def max_trial_count(self):
        """Gets the max_trial_count of this V1beta1ExperimentSpec.  # noqa: E501

        Max completed trials to mark experiment as succeeded  # noqa: E501

        :return: The max_trial_count of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_trial_count

    @max_trial_count.setter
    def max_trial_count(self, max_trial_count):
        """Sets the max_trial_count of this V1beta1ExperimentSpec.

        Max completed trials to mark experiment as succeeded  # noqa: E501

        :param max_trial_count: The max_trial_count of this V1beta1ExperimentSpec.  # noqa: E501
        :type: int
        """

        self._max_trial_count = max_trial_count

    @property
    def metrics_collector_spec(self):
        """Gets the metrics_collector_spec of this V1beta1ExperimentSpec.  # noqa: E501

        Describes the specification of the metrics collector  # noqa: E501

        :return: The metrics_collector_spec of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: V1beta1MetricsCollectorSpec
        """
        return self._metrics_collector_spec

    @metrics_collector_spec.setter
    def metrics_collector_spec(self, metrics_collector_spec):
        """Sets the metrics_collector_spec of this V1beta1ExperimentSpec.

        Describes the specification of the metrics collector  # noqa: E501

        :param metrics_collector_spec: The metrics_collector_spec of this V1beta1ExperimentSpec.  # noqa: E501
        :type: V1beta1MetricsCollectorSpec
        """

        self._metrics_collector_spec = metrics_collector_spec

    @property
    def nas_config(self):
        """Gets the nas_config of this V1beta1ExperimentSpec.  # noqa: E501


        :return: The nas_config of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: V1beta1NasConfig
        """
        return self._nas_config

    @nas_config.setter
    def nas_config(self, nas_config):
        """Sets the nas_config of this V1beta1ExperimentSpec.


        :param nas_config: The nas_config of this V1beta1ExperimentSpec.  # noqa: E501
        :type: V1beta1NasConfig
        """

        self._nas_config = nas_config

    @property
    def objective(self):
        """Gets the objective of this V1beta1ExperimentSpec.  # noqa: E501

        Describes the objective of the experiment.  # noqa: E501

        :return: The objective of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: V1beta1ObjectiveSpec
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this V1beta1ExperimentSpec.

        Describes the objective of the experiment.  # noqa: E501

        :param objective: The objective of this V1beta1ExperimentSpec.  # noqa: E501
        :type: V1beta1ObjectiveSpec
        """

        self._objective = objective

    @property
    def parallel_trial_count(self):
        """Gets the parallel_trial_count of this V1beta1ExperimentSpec.  # noqa: E501

        How many trials can be processed in parallel. Defaults to 3  # noqa: E501

        :return: The parallel_trial_count of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: int
        """
        return self._parallel_trial_count

    @parallel_trial_count.setter
    def parallel_trial_count(self, parallel_trial_count):
        """Sets the parallel_trial_count of this V1beta1ExperimentSpec.

        How many trials can be processed in parallel. Defaults to 3  # noqa: E501

        :param parallel_trial_count: The parallel_trial_count of this V1beta1ExperimentSpec.  # noqa: E501
        :type: int
        """

        self._parallel_trial_count = parallel_trial_count

    @property
    def parameters(self):
        """Gets the parameters of this V1beta1ExperimentSpec.  # noqa: E501

        List of hyperparameter configurations.  # noqa: E501

        :return: The parameters of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: list[V1beta1ParameterSpec]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this V1beta1ExperimentSpec.

        List of hyperparameter configurations.  # noqa: E501

        :param parameters: The parameters of this V1beta1ExperimentSpec.  # noqa: E501
        :type: list[V1beta1ParameterSpec]
        """

        self._parameters = parameters

    @property
    def resume_policy(self):
        """Gets the resume_policy of this V1beta1ExperimentSpec.  # noqa: E501

        Describes resuming policy which usually take effect after experiment terminated.  # noqa: E501

        :return: The resume_policy of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: str
        """
        return self._resume_policy

    @resume_policy.setter
    def resume_policy(self, resume_policy):
        """Sets the resume_policy of this V1beta1ExperimentSpec.

        Describes resuming policy which usually take effect after experiment terminated.  # noqa: E501

        :param resume_policy: The resume_policy of this V1beta1ExperimentSpec.  # noqa: E501
        :type: str
        """

        self._resume_policy = resume_policy

    @property
    def trial_template(self):
        """Gets the trial_template of this V1beta1ExperimentSpec.  # noqa: E501

        Template for each run of the trial.  # noqa: E501

        :return: The trial_template of this V1beta1ExperimentSpec.  # noqa: E501
        :rtype: V1beta1TrialTemplate
        """
        return self._trial_template

    @trial_template.setter
    def trial_template(self, trial_template):
        """Sets the trial_template of this V1beta1ExperimentSpec.

        Template for each run of the trial.  # noqa: E501

        :param trial_template: The trial_template of this V1beta1ExperimentSpec.  # noqa: E501
        :type: V1beta1TrialTemplate
        """

        self._trial_template = trial_template

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
        if issubclass(V1beta1ExperimentSpec, dict):
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
        if not isinstance(other, V1beta1ExperimentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
