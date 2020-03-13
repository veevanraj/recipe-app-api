from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test craetinf a new user successfull"""
        email = "test@londonappdev.com"
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
        email=email,
        password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the new email for the user in normalized way """
        email = "test@LONDONAPPDEV.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """creating anew super user"""
        user = get_user_model().objects.create_superuser(
        'test@londonappdev.com',
        'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
