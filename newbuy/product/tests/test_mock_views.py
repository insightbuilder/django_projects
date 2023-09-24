from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from product.views import detail_pdt 
from mixer.backend.django import mixer
from unittest.mock import Mock, patch
from unittest import TestCase
import pytest


class TestView(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestView,cls).setUpClass()
        mixer.blend('product.Product')
        cls.factory = RequestFactory()

    def test_detail_pdt_authenticated(self):
        path = reverse('detail',kwargs={'pk':1})
        request = self.factory.get(path)
        request.user = mixer.blend(User)

        response = detail_pdt(request,pk=1)

        assert response.status_code == 200
    
    def test_detail_pdt_unauthenticated(self):
        path = reverse('detail',kwargs={'pk':1})
        request = self.factory.get(path)
        request.user = AnonymousUser()

        response = detail_pdt(request,pk=1)

        #assert response.status_code == 302
        assert 'accounts/login' in response.url 