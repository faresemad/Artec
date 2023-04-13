from rest_framework import viewsets
from .serializers import *
from .models import *

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(user=self.request.user.id)

class McqAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = McqAnswerSerializer
    
    def get_queryset(self):
        return McqAnswer.objects.filter(student=self.request.user.id)
    
    def get_serializer_context(self):
        context = super(McqAnswerViewSet, self).get_serializer_context()
        context['student'] = self.request.user
        return context

class HandDrawingAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = HandDrawingSerializer
    
    def get_queryset(self):
        return HandDrawingAnswer.objects.filter(student=self.request.user.id)

    def get_serializer_context(self):
        context = super(HandDrawingAnswerViewSet, self).get_serializer_context()
        context['student'] = self.request.user
        return context

class DigitalDrawingAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = DigitalSerializer
    
    def get_queryset(self):
        return DigitalDrawingAnswer.objects.filter(student=self.request.user.id)
    
    def get_serializer_context(self):
        context = super(DigitalDrawingAnswerViewSet, self).get_serializer_context()
        context['student'] = self.request.user
        return context

class PracticeDrawingAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = PracticeSerializer
    
    def get_queryset(self):
        return PracticeDrawingAnswer.objects.filter(student=self.request.user.id)

    def get_serializer_context(self):
        context = super(PracticeDrawingAnswerViewSet, self).get_serializer_context()
        context['student'] = self.request.user
        return context