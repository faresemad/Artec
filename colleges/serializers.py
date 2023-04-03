from rest_framework import serializers
from .models import College, CollegeDepartment

class CollegeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    logo = serializers.ImageField()
    payment_code = serializers.CharField(max_length=20)
    departments = serializers.StringRelatedField(many=True)
    # departments = serializers.PrimaryKeyRelatedField(many=True, queryset=CollegeDepartment.objects.all())

class CollegeDepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    subtitle = serializers.CharField(max_length=255)
    image = serializers.ImageField()