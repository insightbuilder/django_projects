from ..models import Snippet
from django.test import TestCase
from unittest.mock import patch, Mock


class CodeTest(TestCase):
    """Test module of the Code Model"""
    """
    def setUp(self):
        Snippet.objects.create(
            title="test code",code="if (x > 0):" 
        )

    def x_test_code_model(self):

        snip_test = Snippet.objects.get(title="test code")

        self.assertEqual(
            snip_test.title,'test code'
        )
    """


class CodeMockTest(TestCase):
    """Test module of the Code Model"""
    @patch('snippets.models.Snippet.objects.get')
    def test_code_model(self, mock_snippet):
        mock_snippet.return_value = {"title": "test code",
                                     "code": "if (x > 0):"}

        snip_test = Snippet.objects.get(title="test code")

        self.assertEqual(
            snip_test['title'], 'testcode'
        )
        mock_snippet.was_called_once_with(title="test code")