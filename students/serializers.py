from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class McqAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=MCQExam.objects.none())
    # student = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = McqAnswer
        fields = ['question', 'answer']
        
    def __init__(self, *args, **kwargs):
        super(McqAnswerSerializer, self).__init__(*args, **kwargs)
        self.fields['question'].queryset = MCQExam.objects.filter(college=self.context['request'].user.student.college)
    
    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user.student
        try:
            answer = McqAnswer.objects.get(student=validated_data['student'], question=validated_data['question'])
            answer.answer = validated_data['answer']
            answer.save()
            return answer
        
        except McqAnswer.DoesNotExist:
            return McqAnswer.objects.create(**validated_data)

class HandDrawingSerializer(serializers.ModelSerializer):
    hand_draw = serializers.PrimaryKeyRelatedField(queryset=HandDrawingExam.objects.none())
    class Meta:
        model = HandDrawingAnswer
        fields = ['hand_draw', 'answer']
    
    def __init__(self, *args, **kwargs):
        super(HandDrawingSerializer, self).__init__(*args, **kwargs)
        self.fields['hand_draw'].queryset = HandDrawingExam.objects.filter(college=self.context['request'].user.student.college)
    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user.student
        try:
            answer = HandDrawingAnswer.objects.get(student=validated_data['student'], hand_draw=validated_data['hand_draw'])
            answer.answer = validated_data['answer']
            answer.save()
            return answer
        
        except HandDrawingAnswer.DoesNotExist:
            return HandDrawingAnswer.objects.create(**validated_data)

class DigitalSerializer(serializers.ModelSerializer):
    digital_draw = serializers.PrimaryKeyRelatedField(queryset=DigitalDrawingExam.objects.none())
    class Meta:
        model = DigitalDrawingAnswer
        fields = ['digital_draw', 'answer']
    
    def __init__(self, *args, **kwargs):
        super(DigitalSerializer, self).__init__(*args, **kwargs)
        self.fields['digital_draw'].queryset = DigitalDrawingExam.objects.filter(college=self.context['request'].user.student.college)
    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user.student
        try:
            answer = DigitalDrawingAnswer.objects.get(student=validated_data['student'], digital_draw=validated_data['digital_draw'])
            answer.answer = validated_data['answer']
            answer.save()
            return answer
        
        except DigitalDrawingAnswer.DoesNotExist:
            return DigitalDrawingAnswer.objects.create(**validated_data)

class PracticeSerializer(serializers.ModelSerializer):
    practice_draw = serializers.PrimaryKeyRelatedField(queryset=PracticeDrawingExam.objects.none())
    class Meta:
        model = PracticeDrawingAnswer
        fields = ['practice_draw', 'answer']
    
    def __init__(self, *args, **kwargs):
        super(PracticeSerializer, self).__init__(*args, **kwargs)
        self.fields['practice_draw'].queryset = PracticeDrawingExam.objects.filter(college=self.context['request'].user.student.college)
    
    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user.student
        try:
            answer = PracticeDrawingAnswer.objects.get(student=validated_data['student'], practice_draw=validated_data['practice_draw'])
            answer.answer = validated_data['answer']
            answer.save()
            return answer
        
        except PracticeDrawingAnswer.DoesNotExist:
            return PracticeDrawingAnswer.objects.create(**validated_data)