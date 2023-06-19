from django.test import TestCase

from colleges.models import College
from exams.models import (
    DigitalDrawingExam,
    HandDrawingExam,
    MCQExam,
    PracticeDrawingExam,
)


class ExamModelTestCase(TestCase):
    def setUp(self):
        self.college = College.objects.create(
            name="Test College", logo="test_logo.png", payment_code="test123"
        )

    def test_mcq_exam_model(self):
        exam = MCQExam.objects.create(
            question="What is 2+2?",
            option1="1",
            option2="2",
            option3="4",
            answer="4",
            college=self.college,
        )
        self.assertEqual(str(exam), "What is 2+2?")

    def test_digital_drawing_exam_model(self):
        exam = DigitalDrawingExam.objects.create(
            question="Draw a tree",
            task_description="Using digital tools, draw a tree that looks realistic",
            college=self.college,
        )
        self.assertEqual(str(exam), "Draw a tree")

    def test_hand_drawing_exam_model(self):
        exam = HandDrawingExam.objects.create(
            question="Draw a face",
            task_description="Using pencil and paper, draw a realistic face",
            college=self.college,
        )
        self.assertEqual(str(exam), "Draw a face")

    def test_practice_drawing_exam_model(self):
        exam = PracticeDrawingExam.objects.create(
            question="Draw a circle",
            task_description="Using any medium, draw a perfect circle",
            college=self.college,
        )
        self.assertEqual(str(exam), "Draw a circle")
