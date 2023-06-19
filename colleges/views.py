from rest_framework import viewsets

from .models import College, CollegeDepartment
from .serializers import CollegeDepartmentSerializer, CollegeSerializer


class CollegeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeDepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CollegeDepartmentSerializer

    def get_queryset(self):
        return CollegeDepartment.objects.filter(colleges=self.kwargs["colleges_pk"])
