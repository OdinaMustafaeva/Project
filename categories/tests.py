from django.test import TestCase, Client
from django.urls import reverse

from categories.models import Category

client = Client()


class TestCategory(TestCase):
    def setUp(self) -> None:
        parent = Category.objects.create(title="parent1")
        self.category = Category.objects.create(
            title="cat1",
            position=1,
            parent=parent
        )
        self.new_category_data = {
            "title": "cat_1",
            "position": 1,
            "parent": "parent1"
        }

    def test_category_list(self):
        url = reverse("categories-list-create")

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["title"], self.category.title)

    def test_category_create(self):
        url = reverse("categories-list-create")

        response = client.post(url, data=self.new_category_data)

        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.status_code, 400)
        self.assertEqual(response.data["title"], self.new_category_data["title"])

    def test_category_detail(self):
        url = reverse("category-detail", kwargs={"pk": self.category.id})

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.category.title, "cat1")

    def test_category_update(self):
        url = reverse("category-detail", kwargs={"pk": self.category.id})
        data = {
            "title": "cat-1-edit",
            "position": 1,
            "parent": "parent1"
        }
        response = client.put(url, data=data, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], data["title"])
