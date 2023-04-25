from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerTestCase(TestCase):

    def setUp(self):
        self.user_model = get_user_model()

    def test_create_user(self):
        user = self.user_model.objects.create_user(email='test@example.com', name='Test User', password='testpassword')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.name, 'Test User')
        self.assertTrue(user.check_password('testpassword'))

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            self.user_model.objects.create_user(email='', name='Test User', password='testpassword')

    def test_create_superuser(self):
        superuser = self.user_model.objects.create_superuser(email='admin@example.com', name='Admin User', password='adminpassword')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertEqual(superuser.name, 'Admin User')
        self.assertTrue(superuser.check_password('adminpassword'))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class UserAccountTestCase(TestCase):

    def setUp(self):
        self.user_model = get_user_model()

    def test_get_full_name(self):
        user = self.user_model.objects.create_user(email='test@example.com', name='Test User', password='testpassword')
        self.assertEqual(user.get_full_name(), 'Test User')

    def test_get_short_name(self):
        user = self.user_model.objects.create_user(email='test@example.com', name='Test User', password='testpassword')
        self.assertEqual(user.get_short_name(), 'Test User')

    def test_str(self):
        user = self.user_model.objects.create_user(email='test@example.com', name='Test User', password='testpassword')
        self.assertEqual(str(user), 'test@example.com')
