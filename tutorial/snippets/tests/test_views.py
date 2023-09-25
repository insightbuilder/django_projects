import json
from unittest.mock import Mock, patch
from rest_framework import status
from rest_framework.response import Response
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Snippet
from ..serializers import SnippetSerializer

client = Client()


class GetAllSnippets(TestCase):
    """Test to get all the Snippets"""
    def setUp(self):
        self.snip1 = Snippet.objects.create(
            title='first code',code='i = 1'
        )
        self.snip2= Snippet.objects.create(
            title='second code',code='i = 2'
        )
    
    def x_test_all_snippets(self):

        response = client.get(reverse('snippets'))

        snippets = Snippet.objects.all()
        # print(snippets[0].title)
        serializer = SnippetSerializer(snippets, many=True)

        self.assertEqual(response.json(),serializer.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def x_test_get_single_snippet(self):
        res = client.get(reverse('snippet_detail', kwargs={'pk': 1}))
        snip = Snippet.objects.get(pk = self.snip1.pk)
        serializer = SnippetSerializer(snip)
        self.assertEqual(res.json(), serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def x_test_get_ivalid_snippet(self):
        res = client.get(reverse('snippet_detail',kwargs={'pk': 11}))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewSnippet(TestCase):
    """Test the module of posting snippets"""

    def setUp(self):
        self.valid_payload = {
            "title": 'valid title',
            "code": 'for x in range(y)'
        }

    def x_test_create_snippet(self):
        res = client.post(
            reverse('snippets'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


class GetAllMockSnippets(TestCase):
    """Test to get all the Snippets"""

    @patch(target='snippets.views.SnippetList', method='get', return_value=Response) 
    @patch('snippets.models.Snippet.objects')
    def x_test_all_snippets(self, mock_snips, mock_views):
        resp_data = [{
            'id': 1,
            'title': 'first code',
            'code': 'i = 1',
            'linenos': False,
            'language': 'python',
            'style': 'friendly'}, 
            {'id': 2,
             'title': 'second code',
             'code': 'i = 2',
             'linenos': False,
             'language': 'python',
             'style': 'friendly'}]

        mock_snips.all().return_values.values().return_values = resp_data

        mock_views.return_values = Mock(data=resp_data,
                                           headers={"Content-type": "applicatio/json"},
                                           status=status.HTTP_200_OK,)

        response = client.get(reverse('snippets'))

        print('This response', response)

        self.assertEqual(response.json(), mock_snips.return_values)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
