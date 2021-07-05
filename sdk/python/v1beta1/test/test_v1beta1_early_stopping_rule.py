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
from kubeflow.katib.models.v1beta1_early_stopping_rule import V1beta1EarlyStoppingRule  # noqa: E501
from kubeflow.katib.rest import ApiException

class TestV1beta1EarlyStoppingRule(unittest.TestCase):
    """V1beta1EarlyStoppingRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1EarlyStoppingRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = katib.models.v1beta1_early_stopping_rule.V1beta1EarlyStoppingRule()  # noqa: E501
        if include_optional :
            return V1beta1EarlyStoppingRule(
                comparison = '0', 
                name = '0', 
                start_step = 56, 
                value = '0'
            )
        else :
            return V1beta1EarlyStoppingRule(
        )

    def testV1beta1EarlyStoppingRule(self):
        """Test V1beta1EarlyStoppingRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
