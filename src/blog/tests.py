from django.test import TestCase


class HomePageTest(TestCase):
    def test_open_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/home.html')


class AboutPageTest(TestCase):
    def test_open_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/about.html')