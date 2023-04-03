from rest_framework import viewsets
from .serializers import *

class McqViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MCQExam.objects.all()
    serializer_class = McqExamSerializer

class DigitalDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DigitalDrawingExam.objects.all()
    serializer_class = DigitalDrawingExamSerializer

class HandDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HandDrawingExam.objects.all()
    serializer_class = HandDrawingExamSerializer

class PracticeDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PracticeDrawingExam.objects.all()
    serializer_class = PracticeDrawingExamSerializer