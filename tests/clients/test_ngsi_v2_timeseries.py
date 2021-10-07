"""
@author Thomas Storek

Tests for time series api client aka QuantumLeap
"""
import logging
import unittest
from random import random

import requests

from filip.clients.ngsi_v2 import \
    ContextBrokerClient, \
    QuantumLeapClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.context import ContextEntity
from filip.models.ngsi_v2.subscriptions import Message
from tests.config import settings

logger = logging.getLogger(__name__)


class TestTimeSeries(unittest.TestCase):
    """
    Test class for time series api client
    """
    def setUp(self) -> None:
        """
        Setup test data
        Returns:
            None
        """
        self.fiware_header = FiwareHeader(service=settings.FIWARE_SERVICE,
                                          service_path=settings.FIWARE_SERVICEPATH)
        self.ql_client = QuantumLeapClient(
            url=settings.QL_URL,
            fiware_header=self.fiware_header)
        self.attr = {'temperature': {'value': random(),
                                     'type': 'Number'},
                     'humidity': {'value': random(),
                                  'type': 'Number'},
                     'co2': {'value': random(),
                             'type': 'Number'}}
        self.entity_1 = ContextEntity(id='Kitchen', type='Room', **self.attr)
        self.entity_2 = ContextEntity(id='LivingRoom', type='Room', **self.attr)
        self.cb_client = ContextBrokerClient(
            url=settings.CB_URL,
            fiware_header=self.fiware_header)

        self.cb_client.post_entity(entity=self.entity_1)
        self.cb_client.post_entity(entity=self.entity_2)

    def test_meta_endpoints(self) -> None:
        """
        Test meta data endpoints
        Returns:
            None
        """
        with QuantumLeapClient(
                url=settings.QL_URL,
                fiware_header=self.fiware_header) \
                as client:
            self.assertIsNotNone(client.get_version())
            self.assertIsNotNone(client.get_health())

    def test_input_endpoints(self) -> None:
        """
        Test input endpoint
        Returns:
            None
        """
        with QuantumLeapClient(
                url=settings.QL_URL,
                fiware_header=self.fiware_header) \
                as client:
            data = [self.entity_1, self.entity_2]
            notification_message = Message(data=data, subscriptionId="test")
            client.post_subscription(entity_id=self.entity_1.id)
            client.post_notification(notification_message)

    def test_entity_context(self) -> None:
        """
        Test entities endpoint
        Returns:
            None
        """
        with QuantumLeapClient(
                url=settings.QL_URL,
                fiware_header=self.fiware_header) \
                as client:
            entities = client.get_entities(entity_type='Room')
            for entity in entities:
                print(entity.json(indent=2))

    def test_query_endpoints(self) -> None:
        """
        Test queries
        Returns:
            None
        """
        with QuantumLeapClient(url=settings.QL_URL,
                               fiware_header=self.fiware_header) \
                as client:


            for i in range(10):
                self.entity_1.co2.value = random()
                self.entity_1.humidity.value = random()
                self.entity_1.temperature.value = random()
                self.entity_2.co2.value = random()
                self.entity_2.humidity.value = random()
                self.entity_2.temperature.value = random()

                data = [self.entity_1, self.entity_2]
                notification_message = Message(data=data,
                                               subscriptionId="test")
                client.post_notification(notification_message)

            with self.assertRaises(requests.RequestException):
                client.get_entity_by_id(entity_id=self.entity_1.id,
                                        entity_type='MyType')
            attrs_id = client.get_entity_by_id(entity_id=self.entity_1.id,
                                               aggr_period='minute',
                                               aggr_method='avg',
                                               attrs='temperature,co2')
            logger.info(attrs_id.json(indent=2))
            logger.info(attrs_id.to_pandas())

            attrs_values_id = client.get_entity_values_by_id(
                entity_id=self.entity_1.id)
            logger.info(attrs_values_id.to_pandas())

            attr_id = client.get_entity_attr_by_id(
                entity_id=self.entity_1.id, attr_name="temperature")
            logger.info(attr_id.to_pandas())

            attr_values_id = client.get_entity_attr_values_by_id(
                entity_id=self.entity_1.id, attr_name="temperature")
            logger.info(attr_values_id.to_pandas())

            attrs_type = client.get_entity_by_type(
                entity_type=self.entity_1.type)
            for entity in attrs_type:
                logger.info(entity.to_pandas())

            attrs_values_type = client.get_entity_values_by_type(
                 entity_type=self.entity_1.type)
            for entity in attrs_values_type:
                logger.info(entity.to_pandas())

            attr_type = client.get_entity_attr_by_type(
                entity_type=self.entity_1.type, attr_name="temperature")
            for entity in attr_type:
                logger.info(entity.to_pandas())

            attr_values_type = client.get_entity_attr_values_by_type(
                entity_type=self.entity_1.type, attr_name="temperature")
            for entity in attr_values_type:
                logger.info(entity.to_pandas())

    def tearDown(self) -> None:
        """
        Clean up server
        Returns:
            None
        """
        try:
            for sub in self.cb_client.get_subscription_list():
                self.cb_client.delete_subscription(sub.id)
        except:
            pass
        for entity in self.cb_client.get_entity_list():
            try:
                self.cb_client.delete_entity(entity_id=entity.id,
                                             entity_type=entity.type)
                self.ql_client.delete_entity(entity_id=entity.id,
                                             entity_type=entity.type)
            except:
                pass

        self.ql_client.close()
        self.cb_client.close()
