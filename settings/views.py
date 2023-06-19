from rest_framework import viewsets

from .models import About
from .serializers import AboutSerializer


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
