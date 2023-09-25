from django.urls import reverse
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient 
from ..models import Thread
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

client = APIClient()


class AssistedResearchViewTestCase(SimpleTestCase):

    @patch('django.contrib.auth.models.User',)
    def setUp(self, mock_user):
        self.user = mock_user.objects.create_user(username='testuser',
                                                  password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.assisted_research_url = reverse('assisted_research:assisted-research')
        # Since a thread is created above, the id can be used as 1
        self.assist_research_view_conversation_url = reverse('assisted_research:assist-research-conversation',
                                                             kwargs={'thread_id': 1})
        self.assist_research_view_conversation_url_invalid = reverse('assisted_research:assist-research-conversation',
                                                                     kwargs={'thread_id': 91})
    @patch('assisted_research.models.Thread.objects')
    def test_ar_conversation_view_get_with_thread_id(self, mock_thread,):
        thread_data = [{
            "user": self.user,
            "buffer": [{"message": "Test Message"}],
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        }]
        mock_thread.all().return_values.values().return_values = thread_data
        response = self.client.get(self.assist_research_view_conversation_url)
        mock_thread.assert_called_once()
        self.assertEqual(response[0].status_code, 200)
