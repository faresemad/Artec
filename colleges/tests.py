from django.test import TestCase
from .models import College, CollegeDepartment

class CollegeModelTest(TestCase):

    def test_string_representation(self):
        college = College(name='ABC University')
        self.assertEqual(str(college), 'ABC University')

    def test_college_department_relationship(self):
        college = College.objects.create(name='ABC University')
        department = CollegeDepartment.objects.create(name='Computer Science', subtitle='CS department', image='image.jpg')
        department.colleges.add(college)
        self.assertEqual(list(college.departments.all()), [department])

class CollegeDepartmentModelTest(TestCase):

    def test_string_representation(self):
        department = CollegeDepartment(name='Computer Science', subtitle='CS department', image='image.jpg')
        self.assertEqual(str(department), 'Computer Science')

    def test_college_relationship(self):
        college = College.objects.create(name='ABC University')
        department = CollegeDepartment.objects.create(name='Computer Science', subtitle='CS department', image='image.jpg')
        department.colleges.add(college)
        self.assertEqual(list(department.colleges.all()), [college])
