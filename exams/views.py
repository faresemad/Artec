from rest_framework import viewsets
from .serializers import *

class McqViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = MCQExam.objects.all()
    serializer_class = McqExamSerializer
    
    def get_queryset(self):
        college_id = self.request.user.student.college_id
        return MCQExam.objects.filter(college_id=college_id)

class DigitalDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = DigitalDrawingExam.objects.all()
    serializer_class = DigitalDrawingExamSerializer
    def get_queryset(self):
        college_id = self.request.user.student.college_id
        return DigitalDrawingExam.objects.filter(college_id=college_id)

class HandDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = HandDrawingExam.objects.all()
    serializer_class = HandDrawingExamSerializer
    def get_queryset(self):
        college_id = self.request.user.student.college_id
        return HandDrawingExam.objects.filter(college_id=college_id)

class PracticeDrawingViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = PracticeDrawingExam.objects.all()
    serializer_class = PracticeDrawingExamSerializer
    def get_queryset(self):
        college_id = self.request.user.student.college_id
        return PracticeDrawingExam.objects.filter(college_id=college_id)