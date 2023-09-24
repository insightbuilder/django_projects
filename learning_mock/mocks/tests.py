from unittest import mock
import requests
#from rest_framework import status
#from rest_framework.reverse import reverse
#from rest_framework.test import APIClient
from django.test import Client
from django.urls import reverse


def mocked_requests_get(*args, **kwargs):
    """Put every requests to Platform to here"""

    class MockResponse:
        def __init__(self, json_data, status_code, **kwargs):
            self.json_data = json_data
            self.status_code = status_code
            self.text = kwargs.get('text')

        def json(self):
            return self.json_data

    return MockResponse({'id': 999, 'email': 'good@platform.com'}, 
                        status_code=200)

@mock.patch('views.requests.get', side_effect=mocked_requests_get)
def test_mobile_send_wrong_session_key():
    # client = APIClient()
    client = Client()
    url = reverse('mocks:pdt')
    res = client.get(url)
    assert 200 == res.status_code