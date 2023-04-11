from rest_framework import viewsets
from .serializers import *

class McqViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = McqExamSerializer

    def get_queryset(self):
        college_id = self.kwargs['college_pk']
        return MCQExam.objects.filter(college_id=college_id)

class DigitalDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DigitalDrawingExamSerializer

    def get_queryset(self):
        college_id = self.kwargs['college_pk']
        return DigitalDrawingExam.objects.filter(college_id=college_id)

class HandDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HandDrawingExamSerializer

    def get_queryset(self):
        college_id = self.kwargs['college_pk']
        return HandDrawingExam.objects.filter(college_id=college_id)

class PracticeDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PracticeDrawingExamSerializer

    def get_queryset(self):
        college_id = self.kwargs['college_pk']
        return PracticeDrawingExam.objects.filter(college_id=college_id)