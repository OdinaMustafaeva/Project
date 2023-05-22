from django.test import TestCase, Client
from django.urls import reverse

from blogs.models import Blog
from categories.models import Category
from users.models import User

client = Client()


class TestBlog(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(title="category1")
        author = User.objects.create(email="example@gmail.com", password="1234")
        self.blog = Blog.objects.create(
            title="Blog1",
            author=author,
            body="hello everyone!",
            category=category
        )
        self.new_blog_data = {
            'title': "Blog1",
            'author': 'example@gmail.com',
            'body': "hello everyone!",
            'category': 'category1'
        }

    def test_blog_list(self):
        url = reverse("blog_list_create")

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["title"], self.blog.title)

    def test_blog_create(self):
        url = reverse("blog_list_create")

        response = client.post(url, data=self.new_blog_data)

        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.status_code, 400)
        self.assertEqual(response.data["title"], self.new_blog_data["title"])

    def test_blog_detail(self):
        url = reverse("blog_detail", kwargs={"slug": self.blog.slug})

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.blog.title, "Blog1")

    def test_blog_update(self):
        url = reverse("blog_detail", kwargs={"slug": self.blog.slug})
        data = {
            'title': "Blog1-edited",
            'author': 'example@gmail.com',
            'body': "hello everyone! , edited",
            'category': 'category1'
        }
        response = client.put(url, data=data, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], data["title"])
