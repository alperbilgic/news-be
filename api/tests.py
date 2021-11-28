import json
import tempfile

from rest_framework.test import APITestCase
from django.conf import settings
from rest_framework import status
from PIL import Image


class NewsTestCase(APITestCase):
    def list_news(self, limit, offset, count):
        url = settings.BASE_URL + "api/news/"
        if limit and offset:
            url = url + "?limit=" + limit + "&offset=" + offset
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if count:
            response_data = json.loads(response.content)
            self.assertEqual(response_data.get('count', None), count)

    def create_news(self, title):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        data = {
            "title": title,
            "content": "Lorem ipsum content",
            "detail": "Lorem ipsum detail",
            "date": "2021-11-21T18:50:00Z",
            "image": tmp_file
        }
        response = self.client.post(settings.BASE_URL + "api/news/", data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if response.status_code == status.HTTP_201_CREATED:
            response_data = json.loads(response.content)
            created_id = response_data.get("id", None)
            self.latest_created = created_id

    def update_news(self, title, id):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        data = {
            "title": title,
            "content": "Lorem ipsum content",
            "detail": "Lorem ipsum detail",
            "date": "2021-11-21T18:50:00Z",
            "image": tmp_file
        }
        response = self.client.put(settings.BASE_URL + "api/news/" + id + "/", data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def delete_news(self, id):
        response = self.client.delete(settings.BASE_URL + "api/news/" + id + "/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def search_news(self, search, count):
        url = settings.BASE_URL + "api/news/?title=" + search
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if response.status_code == status.HTTP_200_OK:
            self.assertEqual(response_data.get('count', None), count)

    def test_news(self):
        self.create_news("First News Title")
        self.create_news("Second News Title")
        self.create_news("Third News Title")
        self.list_news(10,0,3)
        self.update_news("Fourth Title", self.latest_created)
        self.search_news("Fourth", 1)
        self.delete_news(self.latest_created)
        self.search_news("Fourth", 0)