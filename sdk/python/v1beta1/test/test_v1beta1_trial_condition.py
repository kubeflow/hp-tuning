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
from kubeflow.katib.models.v1beta1_trial_condition import V1beta1TrialCondition  # noqa: E501
from kubeflow.katib.rest import ApiException

class TestV1beta1TrialCondition(unittest.TestCase):
    """V1beta1TrialCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1TrialCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = katib.models.v1beta1_trial_condition.V1beta1TrialCondition()  # noqa: E501
        if include_optional :
            return V1beta1TrialCondition(
                last_transition_time = None, 
                last_update_time = None, 
                message = '0', 
                reason = '0', 
                status = '0', 
                type = '0'
            )
        else :
            return V1beta1TrialCondition(
                status = '0',
                type = '0',
        )

    def testV1beta1TrialCondition(self):
        """Test V1beta1TrialCondition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
