from django.test import TestCase
from .models import Book


# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An Excellent subtitle",
            author="Tom Christies",
            isbn="123456789",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
