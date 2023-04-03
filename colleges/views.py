from rest_framework import viewsets
from .serializers import CollegeSerializer, CollegeDepartmentSerializer
from .models import College, CollegeDepartment

class CollegeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeDepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CollegeDepartment.objects.all()
    serializer_class = CollegeDepartmentSerializer


# class CollegeDepartmentViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = CollegeDepartmentSerializer
#     def get_queryset(self):
#         college_id = self.kwargs.get('college_id')
#         return CollegeDepartment.objects.filter(colleges__id=college_id)
