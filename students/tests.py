from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from colleges.models import College
from exams.models import *
from .models import *
import os

User = get_user_model()


class StudentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com", name="Test User", password="password"
        )
        self.college = College.objects.create(name="Test College", payment_code="12345")
        self.student = Student.objects.create(
            user=self.user,
            full_name="Test Student",
            student_photo="student/test.jpg",
            national_id="12345678901234",
            seat_number=123,
            total=80.5,
            division="1",
            phone_number="123456789",
            college=self.college,
        )

    def test_str(self):
        self.assertEqual(str(self.student), "Test Student")

    def test_division_options(self):
        division_options = dict(self.student._meta.get_field("division").choices)
        self.assertEqual(division_options, {"1": "رياضة", "2": "علوم", "3": "ادبي"})

    def test_unique_fields(self):
        with self.assertRaises(Exception):
            Student.objects.create(
                user=self.user,
                full_name="Test Student2",
                student_photo="student/test2.jpg",
                national_id="12345678901234",  # duplicate national_id
                seat_number=456,
                total=70.5,
                division="2",
                phone_number="123456789",
                college=self.college,
            )


class McqAnswerModelTestCase(TestCase):
    def setUp(self):
        self.college = College.objects.create(name="Test College", payment_code="1234")
        self.user = User.objects.create_user(
            email="test@example.com", password="test1234", name="Test User"
        )
        self.student = Student.objects.create(
            user=self.user,
            full_name="Test Student",
            student_photo="test.jpg",
            national_id="12345678901234",
            seat_number=1,
            total=50.00,
            division="1",
            phone_number="1234567890",
            college=self.college,
        )
        self.exam = MCQExam.objects.create(
            question="Test Question",
            option1="Option 1",
            option2="Option 2",
            option3="Option 3",
            answer="Option 1",
            college=self.college,
        )
        self.answer = McqAnswer.objects.create(
            student=self.student,
            question=self.exam,
            answer="Option 1",
            is_correct=True,
            score=5,
        )

    def test_answer_creation(self):
        answer = McqAnswer.objects.get(id=1)
        self.assertEqual(answer.student, self.student)
        self.assertEqual(answer.question, self.exam)
        self.assertEqual(answer.answer, "Option 1")
        self.assertTrue(answer.is_correct)
        self.assertEqual(answer.score, 5)


class HandDrawingAnswerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a college
        cls.college = College.objects.create(
            name="Test College", logo="test_logo.jpg", payment_code="123456"
        )

        # Create a student user
        cls.student_user = User.objects.create_user(
            email="test_student@example.com",
            name="Test Student",
            password="testpassword",
        )

        # Create a student
        cls.student = Student.objects.create(
            user=cls.student_user,
            full_name="Test Student",
            student_photo="test_student_photo.jpg",
            national_id="12345678901234",
            seat_number=1,
            total=0,
            division="1",
            phone_number="1234567890",
            college=cls.college,
        )

        # Create a hand drawing exam
        cls.hand_drawing_exam = HandDrawingExam.objects.create(
            question="Test question",
            task_description="Test task description",
            college=cls.college,
        )

        # Create a hand drawing answer
        cls.hand_drawing_answer = HandDrawingAnswer.objects.create(
            student=cls.student,
            hand_draw=cls.hand_drawing_exam,
            answer=SimpleUploadedFile(
                "test_hand_drawing_answer.jpg",
                b"file_content",
                content_type="image/jpeg",
            ),
            score=0,
        )

    def test_hand_drawing_answer_str(self):
        hand_drawing_answer = HandDrawingAnswer.objects.create(
            student=self.student, hand_draw=self.hand_drawing_exam, answer="test.png"
        )
        expected_str = f"{self.student.full_name} - {self.hand_drawing_exam.question}"
        self.assertEqual(str(hand_drawing_answer), expected_str)

    def test_hand_drawing_answer_student(self):
        self.assertEqual(self.hand_drawing_answer.student, self.student)

    def test_hand_drawing_answer_hand_draw(self):
        self.assertEqual(self.hand_drawing_answer.hand_draw, self.hand_drawing_exam)

    def test_hand_drawing_answer_answer(self):
        self.assertIsNotNone(self.hand_drawing_answer.answer)

    def test_hand_drawing_answer_score(self):
        self.assertEqual(self.hand_drawing_answer.score, 0)


class DigitalDrawingAnswerModelTest(TestCase):
    def setUp(self):
        self.college = College.objects.create(name="Test College", payment_code="12345")
        self.user = User.objects.create_user(
            email="test@example.com", name="Test User", password="testpass"
        )
        self.student = Student.objects.create(
            user=self.user,
            full_name="Test Student",
            national_id="12345678901234",
            seat_number=100,
            total=80.0,
            division="1",
            phone_number="123456789",
            college=self.college,
        )
        self.drawing_exam = DigitalDrawingExam.objects.create(
            question="Test Drawing Exam",
            task_description="Draw a circle",
            college=self.college,
        )
        self.image = SimpleUploadedFile(
            "test_image.jpg", content=b"file_content", content_type="image/jpg"
        )
        self.digital_drawing_answer = DigitalDrawingAnswer.objects.create(
            student=self.student,
            digital_draw=self.drawing_exam,
            answer=self.image,
            score=0,
        )

    def test_digital_drawing_answer_str(self):
        self.assertEqual(str(self.digital_drawing_answer), "Test Student")

    def test_digital_drawing_answer_student(self):
        self.assertEqual(self.digital_drawing_answer.student, self.student)

    def test_digital_drawing_answer_digital_draw(self):
        self.assertEqual(self.digital_drawing_answer.digital_draw, self.drawing_exam)

    def test_digital_drawing_answer_answer(self):
        generated_name = os.path.basename(self.digital_drawing_answer.answer.name)
        expected_name = os.path.basename(self.image.name)
        self.assertEqual(
            generated_name,
            expected_name,
            "The names of the image files should be equal",
        )

    def test_digital_drawing_answer_score(self):
        self.assertEqual(self.digital_drawing_answer.score, 0)


class PracticeDrawingAnswerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = get_user_model().objects.create_user(
            email="test@example.com", name="Test User", password="testpass"
        )
        cls.college = College.objects.create(
            name="Test College", payment_code="testcode"
        )
        cls.exam = PracticeDrawingExam.objects.create(
            question="Test question", task_description="Test task", college=cls.college
        )
        cls.student = Student.objects.create(
            user=cls.user,
            full_name="Test Student",
            student_photo=SimpleUploadedFile("test_photo.jpg", b"content"),
            national_id="12345678901234",
            seat_number=1,
            total=100.0,
            division="1",
            phone_number="123456789",
            college=cls.college,
        )
        cls.answer = PracticeDrawingAnswer.objects.create(
            student=cls.student,
            practice_draw=cls.exam,
            answer=SimpleUploadedFile("test_answer.jpg", b"content"),
            score=50,
        )

    def test_practice_drawing_answer_str(self):
        self.assertEqual(str(self.answer), self.student.full_name)

    def test_practice_drawing_answer_student(self):
        self.assertEqual(self.answer.student, self.student)

    def test_practice_drawing_answer_practice_draw(self):
        self.assertEqual(self.answer.practice_draw, self.exam)

    def test_practice_drawing_answer_score(self):
        self.assertEqual(self.answer.score, 50)
