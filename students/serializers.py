from rest_framework import serializers
from django.db.models import Sum

from .models import *

class StudentSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.none(), required=False)
    # college = serializers.PrimaryKeyRelatedField(queryset=College.objects.none(), required=False)
    user = serializers.SerializerMethodField()
    college = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['up_to_level','user', 'college']

    def get_user(self, obj):
        return obj.user.email
    def get_college(self, obj):
        return obj.college.name
    
    def __init__(self, instance=None, **kwargs):
        super(StudentSerializer, self).__init__(instance, **kwargs)
        self.fields['user'].queryset = User.objects.filter(id=self.context['request'].user.id)
        self.fields['college'].queryset = College.objects.filter(id=self.context['request'].user.student.college.id)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update_up_to_level(self, student):
        score_sum = student.student_mcq.aggregate(Sum('score'))['score__sum']
        if score_sum is None:
            score_sum = 0
        if score_sum >= 3 and score_sum <= 5:
            student.up_to_level = True
        else:
            student.up_to_level = False
        student.save()
    
    def to_representation(self, instance):
        self.update_up_to_level(instance)
        return super().to_representation(instance)

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
            prev_answer = answer.answer
            answer.answer = validated_data['answer']
            if answer.answer == answer.question.answer:
                if prev_answer != answer.answer:
                    answer.score += 1
            else:
                if prev_answer == answer.question.answer:
                    answer.score -= 1
        except McqAnswer.DoesNotExist:
            answer = McqAnswer.objects.create(**validated_data)
            if answer.answer == answer.question.answer:
                answer.score += 1
        answer.is_correct = answer.answer == answer.question.answer
        answer.save()
        return answer

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

class UserResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','full_name']

class StudentResultsSerializer(serializers.ModelSerializer):
    user = UserResultSerializer(read_only=True)
    class Meta:
        model = StudentResults
        fields = ['user', 'mcq_result', 'digital_art_result', 'hand_drawing_result', 'trial_result', 'up_to_level']
    
    def __init__(self, *args, **kwargs):
        super(StudentResultsSerializer, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = Student.objects.filter(user_id=self.context['request'].user.id)

    def create(self, validated_data):
        return StudentResults.objects.create(**validated_data)