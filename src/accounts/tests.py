from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    user_class = get_user_model()

    user = {
        "username": "testuser",
        "email": "test@email.com",
        "password": "secret"
    }

    super_user = {
        "username": "testsuperuser",
        "email": "supertest@email.com",
        "password": "supersecret"
    }

    def test_create_user(self):
        user = self.user_class.objects.create_user(
            username=self.user["username"],
            email=self.user["email"],
            password=self.user["password"]
        )
        self.assertEqual(user.username, self.user["username"])
        self.assertEqual(user.email, self.user["email"])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user(self):
        user = self.user_class.objects.create_superuser(
            username=self.super_user["username"],
            email=self.super_user["email"],
            password=self.super_user["password"])
        self.assertEqual(user.username, self.super_user["username"])
        self.assertEqual(user.email, self.super_user["email"])
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
