from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(title="Test post", text="Test post text", author=self.user)

    def test_post_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title[:50])

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test post')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.text}', 'Test post text')

    def test_open_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test post text')
        self.assertTemplateUsed(response, 'blogs/home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test post')
        self.assertTemplateUsed(response, 'blogs/details.html')

        no_response = self.client.get('/post/100000/')
        self.assertEqual(no_response.status_code, 404)


class AboutPageTest(TestCase):
    def test_open_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/about.html')
