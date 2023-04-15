from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.none())
    college = serializers.PrimaryKeyRelatedField(queryset=College.objects.none())
    class Meta:
        model = Student
        fields = '__all__'
    
    def __init__(self, instance=None, **kwargs):
        super(StudentSerializer, self).__init__(instance, **kwargs)
        self.fields['user'].queryset = User.objects.filter(id=self.context['request'].user.id)
        self.fields['college'].queryset = College.objects.filter(id=self.context['request'].user.student.college.id)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

class McqAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=MCQExam.objects.none())
    is_correct = serializers.SerializerMethodField()

    class Meta:
        model = McqAnswer
        fields = ['question', 'answer', 'is_correct']

    def __init__(self, *args, **kwargs):
        super(McqAnswerSerializer, self).__init__(*args, **kwargs)
        self.fields['question'].queryset = MCQExam.objects.filter(college=self.context['request'].user.student.college)

    def get_is_correct(self, obj):
        return obj.is_correct

    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user.student
        try:
            answer = McqAnswer.objects.get(student=validated_data['student'], question=validated_data['question'])
            answer.answer = validated_data['answer']
        except McqAnswer.DoesNotExist:
            answer = McqAnswer.objects.create(**validated_data)
        answer.is_correct = self.check_answer(answer)
        answer.save()
        return answer

    def check_answer(self, answer_instance):
        mcq_exam = answer_instance.question
        if answer_instance.answer == mcq_exam.answer:
            return True
        else:
            return False

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