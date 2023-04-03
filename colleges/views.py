from rest_framework import viewsets
from .serializers import CollegeSerializer, CollegeDepartmentSerializer
from .models import College, CollegeDepartment

class CollegeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeDepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CollegeDepartment.objects.all()
    serializer_class = CollegeDepartmentSerializer