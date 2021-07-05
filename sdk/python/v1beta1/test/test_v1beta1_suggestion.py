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
from kubeflow.katib.models.v1beta1_suggestion import V1beta1Suggestion  # noqa: E501
from kubeflow.katib.rest import ApiException

class TestV1beta1Suggestion(unittest.TestCase):
    """V1beta1Suggestion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1Suggestion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = katib.models.v1beta1_suggestion.V1beta1Suggestion()  # noqa: E501
        if include_optional :
            return V1beta1Suggestion(
                api_version = '0', 
                kind = '0', 
                metadata = None, 
                spec = katib.models./v1beta1/suggestion_spec..v1beta1.SuggestionSpec(
                    algorithm = katib.models.v1beta1/algorithm_spec.v1beta1.AlgorithmSpec(
                        algorithm_name = '0', 
                        algorithm_settings = [
                            katib.models.v1beta1/algorithm_setting.v1beta1.AlgorithmSetting(
                                name = '0', 
                                value = '0', )
                            ], ), 
                    early_stopping = katib.models.v1beta1/early_stopping_spec.v1beta1.EarlyStoppingSpec(
                        algorithm_name = '0', ), 
                    requests = 56, 
                    resume_policy = '0', ), 
                status = katib.models./v1beta1/suggestion_status..v1beta1.SuggestionStatus(
                    algorithm_settings = [
                        katib.models.v1beta1/algorithm_setting.v1beta1.AlgorithmSetting(
                            name = '0', 
                            value = '0', )
                        ], 
                    completion_time = None, 
                    conditions = [
                        katib.models./v1beta1/suggestion_condition..v1beta1.SuggestionCondition(
                            last_transition_time = None, 
                            last_update_time = None, 
                            message = '0', 
                            reason = '0', 
                            status = '0', 
                            type = '0', )
                        ], 
                    last_reconcile_time = None, 
                    start_time = None, 
                    suggestion_count = 56, 
                    suggestions = [
                        katib.models./v1beta1/trial_assignment..v1beta1.TrialAssignment(
                            early_stopping_rules = [
                                katib.models.v1beta1/early_stopping_rule.v1beta1.EarlyStoppingRule(
                                    comparison = '0', 
                                    name = '0', 
                                    start_step = 56, 
                                    value = '0', )
                                ], 
                            name = '0', 
                            parameter_assignments = [
                                katib.models.v1beta1/parameter_assignment.v1beta1.ParameterAssignment(
                                    name = '0', 
                                    value = '0', )
                                ], )
                        ], )
            )
        else :
            return V1beta1Suggestion(
        )

    def testV1beta1Suggestion(self):
        """Test V1beta1Suggestion"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
