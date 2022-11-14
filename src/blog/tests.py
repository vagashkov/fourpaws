from django.test import TestCase
from django.urls import reverse

from .models import Post


class HomePageTest(TestCase):
    def setUp(self):
        Post.objects.create(caption="Test post", text="Test post text")

    def test_open_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/home.html')


class AboutPageTest(TestCase):
    def test_open_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/about.html')


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(caption="Test post", text="Test post text")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Test post text')
