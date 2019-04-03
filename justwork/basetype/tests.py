from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from .views import PageList, PageDetail


class TestPageList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PageList.as_view()
        self.uri = '/api/v1/pages/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestPageDetail(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_detail(self):
        response = self.client.get('/api/v1/page/1/')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
