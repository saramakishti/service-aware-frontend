# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.entity import Entity  # noqa: E501

class TestEntity(unittest.TestCase):
    """Entity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Entity:
        """Test Entity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Entity`
        """
        model = Entity()  # noqa: E501
        if include_optional:
            return Entity(
                did = 'did:sov:test:1234',
                name = 'C1',
                ip = '127.0.0.1',
                visible = True,
                other = openapi_client.models.other.Other(),
                attached = True
            )
        else:
            return Entity(
                attached = True,
        )
        """

    def testEntity(self):
        """Test Entity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
