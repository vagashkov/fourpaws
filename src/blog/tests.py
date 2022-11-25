from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class SignupPageTest(TestCase):
    username = 'testuser'
    email = 'test@email.com'
    password = 'secret'

    def test_open_signup_page_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_open_signup_page_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username,
                         self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class BlogListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(title="Test post",
                                        text="Test post text",
                                        author=self.user)

    def test_post_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title[:50])

    def test_post_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test post')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.text}', 'Test post text')

    def test_open_post_list_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/home.html')

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

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'New title',
            'author': self.user.id,
            'text': 'New test text'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().text, 'New test text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Edited title',
            'text': 'Edited text'
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)


class AboutPageTest(TestCase):
    def test_open_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/about.html')
