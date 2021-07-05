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
from kubeflow.katib.models.v1beta1_trial import V1beta1Trial  # noqa: E501
from kubeflow.katib.rest import ApiException

class TestV1beta1Trial(unittest.TestCase):
    """V1beta1Trial unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1Trial
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = katib.models.v1beta1_trial.V1beta1Trial()  # noqa: E501
        if include_optional :
            return V1beta1Trial(
                api_version = '0', 
                kind = '0', 
                metadata = None, 
                spec = katib.models./v1beta1/trial_spec..v1beta1.TrialSpec(
                    early_stopping_rules = [
                        katib.models.v1beta1/early_stopping_rule.v1beta1.EarlyStoppingRule(
                            comparison = '0', 
                            name = '0', 
                            start_step = 56, 
                            value = '0', )
                        ], 
                    failure_condition = '0', 
                    metrics_collector = katib.models.v1beta1/metrics_collector_spec.v1beta1.MetricsCollectorSpec(
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
                    parameter_assignments = [
                        katib.models.v1beta1/parameter_assignment.v1beta1.ParameterAssignment(
                            name = '0', 
                            value = '0', )
                        ], 
                    primary_container_name = '0', 
                    primary_pod_labels = {
                        'key' : '0'
                        }, 
                    retain_run = True, 
                    run_spec = None, 
                    success_condition = '0', ), 
                status = katib.models./v1beta1/trial_status..v1beta1.TrialStatus(
                    completion_time = None, 
                    conditions = [
                        katib.models./v1beta1/trial_condition..v1beta1.TrialCondition(
                            last_transition_time = None, 
                            last_update_time = None, 
                            message = '0', 
                            reason = '0', 
                            status = '0', 
                            type = '0', )
                        ], 
                    last_reconcile_time = None, 
                    observation = katib.models.v1beta1/observation.v1beta1.Observation(
                        metrics = [
                            katib.models.v1beta1/metric.v1beta1.Metric(
                                latest = '0', 
                                max = '0', 
                                min = '0', 
                                name = '0', )
                            ], ), 
                    start_time = None, )
            )
        else :
            return V1beta1Trial(
        )

    def testV1beta1Trial(self):
        """Test V1beta1Trial"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
