# api/tests/test_data_analysis.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from io import BytesIO
from PIL import Image


class DataAnalysisTestCase(APITestCase):
    def test_bar_chart(self):
        response = self.client.get(reverse("data-analysis"), {"operation": "bar_chart"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "image/png")
        self._validate_image(response)

    def test_line_chart(self):
        response = self.client.get(
            reverse("data-analysis"), {"operation": "line_chart"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "image/png")
        self._validate_image(response)

    def test_scatter_plot(self):
        response = self.client.get(
            reverse("data-analysis"), {"operation": "scatter_plot"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "image/png")
        self._validate_image(response)

    def _validate_image(self, response):
        image = Image.open(BytesIO(response.content))
        self.assertIsNotNone(image)
        self.assertTrue(image.size[0] > 0)
        self.assertTrue(image.size[1] > 0)
