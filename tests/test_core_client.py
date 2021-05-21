"""
Test for filip.core.client
"""
import unittest
import requests
from pathlib import Path
from filip.core.models import FiwareHeader
from filip.core.client import Client

class TestClient(unittest.TestCase):
    """
    Test case for global client
    """
    def setUp(self) -> None:
        """
        Setup test data
        Returns:
            None
        """
        self.fh = FiwareHeader(service='filip',
                               service_path='/testing')

        self.config = {'cb_url': 'http://134.130.166.184:1026',
                       'iota_url': 'http://134.130.166.184:4041',
                       'ql_url': 'http://134.130.166.184:8668'}

    def test_config_dict(self):
        with requests.Session() as s:
            client=Client(config=self.config, session=s)
            print(client.cb.get_version())

    def test_config_json(self):
        config_path = Path("./test_core_client.json")
        client = Client(config=config_path)
        print(client.cb.get_version())

    def test_env(self):
        pass

    def tearDown(self) -> None:
        """

        Returns:
            pass
        """
        pass