from .serializers import *
from .models import *
from .premission import CreateRetrieveUpdate

class StudentViewSet(CreateRetrieveUpdate):
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(user=self.request.user.id)
    
    def get_serializer_context(self):
        context = super(StudentViewSet, self).get_serializer_context()
        context['user'] = self.request.user
        return context

class McqAnswerViewSet(CreateRetrieveUpdate):
    serializer_class = McqAnswerSerializer
    
    def get_queryset(self):
        return McqAnswer.objects.filter(student=self.request.user.id)
    
    def get_serializer_context(self):
        context = super(McqAnswerViewSet, self).get_serializer_context()
        context['student'] = self.request.user
        return context

class HandDrawingAnswerViewSet(CreateRetrieveUpdate):
    serializer_class = HandDrawingSerializer
    
    def get_queryset(self):
        return HandDrawingAnswer.objects.filter(student=self.request.user.id)

    def get_serializer_context(self):
        context = super(HandDrawingAnswerViewSet, self).get_serializer_context()
        context['student'] = self.request.user
        return context

class DigitalDrawingAnswerViewSet(CreateRetrieveUpdate):
    serializer_class = DigitalSerializer
    
    def get_queryset(self):
        return DigitalDrawingAnswer.objects.filter(student=self.request.user.id)
    
    def get_serializer_context(self):
        context = super(DigitalDrawingAnswerViewSet, self).get_serializer_context()
        context['student'] = self.request.user
        return context

class PracticeDrawingAnswerViewSet(CreateRetrieveUpdate):
    serializer_class = PracticeSerializer
    
    def get_queryset(self):
        return PracticeDrawingAnswer.objects.filter(student=self.request.user.id)

    def get_serializer_context(self):
        context = super(PracticeDrawingAnswerViewSet, self).get_serializer_context()
        context['student'] = self.request.user
        return context