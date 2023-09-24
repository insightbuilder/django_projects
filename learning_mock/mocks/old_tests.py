from django.test import Client, TestCase
from unittest.mock import patch, Mock, MagicMock
from django.urls import reverse
from mocks.views import Product
from rest_framework.response import Response

class SimpleTestView(TestCase):

    def setUp(self):
        self.pdt_url = reverse('pdt')
   
    @patch('mocks.views.Product.objects.all')
    def test_mocked_product(self, mock_product):
        response = self.client.get(self.pdt_url)
        print(response.status_code)
        self.assertEquals(mock_product.called_once(), True)

    @patch('mocks.views.Response', autospec=True)
    def test_mocked_product_reponse(self, mock_rest_response):
        mock_response_ret = MagicMock(spec=Response)

        mock_response_ret.status_code = 200
        mock_response_ret.data = {"message":'New World'}
        mock_rest_response.return_value = mock_response_ret

        response = self.client.get(self.pdt_url)

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data, {"message":"New World"})

        mock_rest_response.called_once()