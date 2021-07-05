# coding: utf-8

"""
    Katib

    Swagger description for Katib  # noqa: E501

    The version of the OpenAPI document: v1beta1-0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubeflow.katib
from kubeflow.katib.models.v1beta1_experiment_spec import V1beta1ExperimentSpec  # noqa: E501
from kubeflow.katib.rest import ApiException

class TestV1beta1ExperimentSpec(unittest.TestCase):
    """V1beta1ExperimentSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1ExperimentSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = katib.models.v1beta1_experiment_spec.V1beta1ExperimentSpec()  # noqa: E501
        if include_optional :
            return V1beta1ExperimentSpec(
                algorithm = katib.models.v1beta1/algorithm_spec.v1beta1.AlgorithmSpec(
                    algorithm_name = '0', 
                    algorithm_settings = [
                        katib.models.v1beta1/algorithm_setting.v1beta1.AlgorithmSetting(
                            name = '0', 
                            value = '0', )
                        ], ), 
                early_stopping = katib.models.v1beta1/early_stopping_spec.v1beta1.EarlyStoppingSpec(
                    algorithm_name = '0', 
                    algorithm_settings = [
                        katib.models.v1beta1/early_stopping_setting.v1beta1.EarlyStoppingSetting(
                            name = '0', 
                            value = '0', )
                        ], ), 
                max_failed_trial_count = 56, 
                max_trial_count = 56, 
                metrics_collector_spec = katib.models.v1beta1/metrics_collector_spec.v1beta1.MetricsCollectorSpec(
                    collector = katib.models.v1beta1/collector_spec.v1beta1.CollectorSpec(
                        custom_collector = None, 
                        kind = '0', ), 
                    source = katib.models.v1beta1/source_spec.v1beta1.SourceSpec(
                        file_system_path = katib.models.v1beta1/file_system_path.v1beta1.FileSystemPath(
                            kind = '0', 
                            path = '0', ), 
                        filter = katib.models.v1beta1/filter_spec.v1beta1.FilterSpec(
                            metrics_format = [
                                '0'
                                ], ), 
                        http_get = None, ), ), 
                nas_config = katib.models.v1beta1/nas_config.v1beta1.NasConfig(
                    graph_config = katib.models.v1beta1/graph_config.v1beta1.GraphConfig(
                        input_sizes = [
                            56
                            ], 
                        num_layers = 56, 
                        output_sizes = [
                            56
                            ], ), 
                    operations = [
                        katib.models.v1beta1/operation.v1beta1.Operation(
                            operation_type = '0', 
                            parameters = [
                                katib.models.v1beta1/parameter_spec.v1beta1.ParameterSpec(
                                    feasible_space = katib.models.v1beta1/feasible_space.v1beta1.FeasibleSpace(
                                        list = [
                                            '0'
                                            ], 
                                        max = '0', 
                                        min = '0', 
                                        step = '0', ), 
                                    name = '0', 
                                    parameter_type = '0', )
                                ], )
                        ], ), 
                objective = katib.models.v1beta1/objective_spec.v1beta1.ObjectiveSpec(
                    additional_metric_names = [
                        '0'
                        ], 
                    goal = 1.337, 
                    metric_strategies = [
                        katib.models.v1beta1/metric_strategy.v1beta1.MetricStrategy(
                            name = '0', 
                            value = '0', )
                        ], 
                    objective_metric_name = '0', 
                    type = '0', ), 
                parallel_trial_count = 56, 
                parameters = [
                    katib.models.v1beta1/parameter_spec.v1beta1.ParameterSpec(
                        feasible_space = katib.models.v1beta1/feasible_space.v1beta1.FeasibleSpace(
                            list = [
                                '0'
                                ], 
                            max = '0', 
                            min = '0', 
                            step = '0', ), 
                        name = '0', 
                        parameter_type = '0', )
                    ], 
                resume_policy = '0', 
                trial_template = katib.models.v1beta1/trial_template.v1beta1.TrialTemplate(
                    config_map = katib.models.v1beta1/config_map_source.v1beta1.ConfigMapSource(
                        config_map_name = '0', 
                        config_map_namespace = '0', 
                        template_path = '0', ), 
                    failure_condition = '0', 
                    primary_container_name = '0', 
                    primary_pod_labels = {
                        'key' : '0'
                        }, 
                    retain = True, 
                    success_condition = '0', 
                    trial_parameters = [
                        katib.models.v1beta1/trial_parameter_spec.v1beta1.TrialParameterSpec(
                            description = '0', 
                            name = '0', 
                            reference = '0', )
                        ], 
                    trial_spec = None, )
            )
        else :
            return V1beta1ExperimentSpec(
        )

    def testV1beta1ExperimentSpec(self):
        """Test V1beta1ExperimentSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
