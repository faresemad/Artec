from rest_framework import viewsets
from .serializers import CollegeSerializer
from .models import College

class CollegeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer