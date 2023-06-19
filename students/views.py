from .models import (
    DigitalDrawingAnswer,
    HandDrawingAnswer,
    McqAnswer,
    PracticeDrawingAnswer,
    Student,
    StudentResults,
)
from .premission import CreateRetrieveUpdate, RetrieveUpdate
from .serializers import (
    DigitalSerializer,
    HandDrawingSerializer,
    McqAnswerSerializer,
    PracticeSerializer,
    StudentResultsSerializer,
    StudentSerializer,
)


class StudentViewSet(CreateRetrieveUpdate):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class McqAnswerViewSet(CreateRetrieveUpdate):
    serializer_class = McqAnswerSerializer

    def get_queryset(self):
        return McqAnswer.objects.filter(student=self.request.user.student.id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["student"] = self.request.user
        return context


class HandDrawingAnswerViewSet(CreateRetrieveUpdate):
    serializer_class = HandDrawingSerializer

    def get_queryset(self):
        return HandDrawingAnswer.objects.filter(student=self.request.user.student.id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["student"] = self.request.user
        return context


class DigitalDrawingAnswerViewSet(CreateRetrieveUpdate):
    serializer_class = DigitalSerializer

    def get_queryset(self):
        return DigitalDrawingAnswer.objects.filter(student=self.request.user.student.id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["student"] = self.request.user
        return context


class PracticeDrawingAnswerViewSet(CreateRetrieveUpdate):
    serializer_class = PracticeSerializer

    def get_queryset(self):
        return PracticeDrawingAnswer.objects.filter(
            student=self.request.user.student.id
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["student"] = self.request.user
        return context


class StudentResultsViewSet(RetrieveUpdate):
    serializer_class = StudentResultsSerializer

    def get_queryset(self):
        student_id = Student.objects.get(user_id=self.request.user.id).id
        return StudentResults.objects.filter(user_id=student_id)
