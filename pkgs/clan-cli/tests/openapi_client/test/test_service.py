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

from openapi_client.models.service import Service  # noqa: E501

class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Service:
        """Test Service
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Service`
        """
        model = Service()  # noqa: E501
        if include_optional:
            return Service(
                uuid = '8e285c0c-4e40-430a-a477-26b3b81e30df',
                service_name = 'Carlos Printing',
                service_type = '3D Printing',
                endpoint_url = 'http://127.0.0.1:8000',
                status = 'unknown',
                other = {action=[register, deregister, delete, create]},
                entity_did = 'did:sov:test:1234',
                entity = openapi_client.models.entity.Entity(
                    did = 'did:sov:test:1234', 
                    name = 'C1', 
                    ip = '127.0.0.1', 
                    visible = True, 
                    other = {network=Carlos Home Network, roles=[service repository, service prosumer]}, 
                    attached = True, )
            )
        else:
            return Service(
                uuid = '8e285c0c-4e40-430a-a477-26b3b81e30df',
                service_name = 'Carlos Printing',
                service_type = '3D Printing',
                endpoint_url = 'http://127.0.0.1:8000',
                status = 'unknown',
                other = {action=[register, deregister, delete, create]},
                entity_did = 'did:sov:test:1234',
                entity = openapi_client.models.entity.Entity(
                    did = 'did:sov:test:1234', 
                    name = 'C1', 
                    ip = '127.0.0.1', 
                    visible = True, 
                    other = {network=Carlos Home Network, roles=[service repository, service prosumer]}, 
                    attached = True, ),
        )
        """

    def testService(self):
        """Test Service"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
