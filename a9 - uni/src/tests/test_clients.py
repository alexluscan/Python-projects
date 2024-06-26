import unittest
from src.domain.client import Client
from src.services.ClientService import ClientService
from src.repository.repository_exception import RepositoryException


class TestCientService(unittest.TestCase):
    def setUp(self):
        self.client_service = ClientService()

    def test_add_client_success(self):
        client_id = 10
        name = "Lionel Messi"
        self.client_service.add_client(client_id, name)
        self.assertEqual(len(self.client_service.get_all_clients()), 20)

    def test_remove_client_success(self):
        client_id = 10
        name = "Lionel Messi"
        self.client_service.add_client(client_id, name)
        self.client_service.remove_client(client_id)
        self.assertEqual(len(self.client_service.get_all_clients()), 19)

    def test_remove_client_failure(self):
        with self.assertRaises(RepositoryException):
            self.client_service.remove_client(99, testing=True)

    def test_update_client_success(self):
        client_id = 20
        name = "Lionel Messi"
        self.client_service.add_client(client_id, name)
        new_name = "THE GOAT"
        self.client_service.update_client(client_id, new_name)
        updated_client = self.client_service.get_all_clients()[client_id]
        self.assertEqual(updated_client.name, new_name)

    def test_update_client_failure(self):
        with self.assertRaises(RepositoryException):
            self.client_service.update_client(511, "Lionel Messi", testing=True)

    def test_update_client_failure(self):
        client_id = 99
        name = "Jr"
        with self.assertRaises(RepositoryException):
            self.client_service.update_client(client_id, name, testing=True)

    def test_get_all_clients(self):
        self.assertEqual(len(self.client_service.get_all_clients()), 20)