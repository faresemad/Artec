from rest_framework import serializers
from .models import College, CollegeDepartment

class CollegeDepartmentSerializer(serializers.ModelSerializer):
    college_name = serializers.SerializerMethodField()

    class Meta:
        model = CollegeDepartment
        fields = ['id', 'name', 'subtitle', 'image', 'college_name']

    def get_college_name(self, obj):
        return obj.colleges.first().name if obj.colleges.exists() else None

class CollegeSerializer(serializers.ModelSerializer):
    departments = CollegeDepartmentSerializer(many=True)

    class Meta:
        model = College
        fields = ['id', 'name', 'logo', 'payment_code', 'departments']