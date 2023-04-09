from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class McqAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = McqAnswer
        fields = '__all__'

class HandDrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandDrawingAnswer
        fields = '__all__'

class DigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalDrawingAnswer
        fields = '__all__'

class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeDrawingAnswer
        fields = '__all__'