from unittest.mock import Mock, patch
from django.test import TestCase, Client
from django.urls import reverse
import requests
from unittest.mock import create_autospec
from rest_framework.test import APIClient

@patch("mocks.views.product_view", autospec=True)
class ProductViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_product(self, mock_pdt_view):
        url = reverse('pdt')
        self.client.get(url)
        self.assertTrue(mock_pdt_view.called)
        print(mock_pdt_view)