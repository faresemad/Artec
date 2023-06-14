from rest_framework import viewsets
from .serializers import AboutSerializer
from .models import About


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
