from django.test import Client, TestCase
from unittest.mock import patch, Mock, MagicMock
from .views import product_view



class SimpleTestView(TestCase):

    def setUp(self):
        self.client = Client()

    
    @patch('mocks.views.Product.objects.all')
    def test_mocked_product_reponse(self, mock_product):
        """
        This is a simple testcase using mock feature.
        1 - Decorate the method with path (app_path.views.module).
        2 - Reference the mock in test method as param (mock_product).
        3 - Define a value of the return of method (sub method or property) to mock.
        4 - Call the mocked method and compare.
        """
        # Create a mock queryset to simulate the database query
        mock_queryset = Mock()
        
        # Configure the mock queryset to be iterable
        mock_queryset.return_value = [{
            "name": 'Product1',
            "price": 10.0,
            "qty": 5
            }]
                
        mock_product.return_value = mock_queryset  

        response = self.client.get('/pdt/')

        self.assertEqual(response.status_code, 200)

        expected_data = [{
            "name": 'name1',
            "price": 25.0,
            "qty": 1
        }]

        self.assertEqual(mock_product.was_called_once)
        #self.assertEqual(response.content, expected_data)
        #self.assertEqual(str(response.content, encoding='utf-8'), expected_data)
