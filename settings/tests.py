from django.test import TestCase
from .models import About

class AboutModelTest(TestCase):

    def setUp(self):
        self.about = About.objects.create(
            title='Test Title',
            description='Test Description',
            email='test@test.com'
        )

    def test_about_model(self):
        self.assertEqual(str(self.about), self.about.title)
        self.assertEqual(self.about.description, 'Test Description')
        self.assertEqual(self.about.email, 'test@test.com')
