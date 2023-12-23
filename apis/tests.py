from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book
from django.urls import reverse


# Create your tests here.
class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for APIs",
            subsitle="Build web APIS with Python and Django",
            author="William S.Vincent",
            isbn="9781735467221",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
