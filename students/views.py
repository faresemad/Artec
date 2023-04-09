from rest_framework import viewsets
from .serializers import *
from .models import *

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class McqAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = McqAnswerSerializer
    queryset = McqAnswer.objects.all()

class HandDrawingAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = HandDrawingSerializer
    queryset = HandDrawingAnswer.objects.all()

class DigitalDrawingAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = DigitalSerializer
    queryset = DigitalDrawingAnswer.objects.all()

class PracticeDrawingAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = PracticeSerializer
    queryset = PracticeDrawingAnswer.objects.all()