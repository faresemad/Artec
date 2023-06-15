from django.contrib.auth import get_user_model
from notifications.models import Notification
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import NotificationSerializer

User = get_user_model()


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(detail=True, methods=["post", "get"])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        if notification.recipient == request.user:
            notification.mark_as_read()
            data = {"success": True}
        else:
            data = {
                "success": False,
                "error": "You are not authorized to mark this notification as read.",
            }
        return Response(data)

    @action(detail=False, methods=["post", "get"])
    def make_all_as_read(self, request):
        Notification.objects.filter(recipient=request.user).mark_all_as_read()
        data = {"success": True}
        return Response(data)

    @action(detail=True, methods=["post", "get"])
    def mark_as_unread(self, request, pk=None):
        notification = self.get_object()
        if notification.recipient == request.user:
            notification.mark_as_unread()
            data = {"success": True}
        else:
            data = {
                "success": False,
                "error": "You are not authorized to mark this notification as unread.",
            }
        return Response(data)

    @action(detail=False, methods=["post", "get"])
    def make_all_as_unread(self, request):
        Notification.objects.filter(recipient=request.user).mark_all_as_unread()
        data = {"success": True}
        return Response(data)

    @action(detail=True, methods=["delete", "get"])
    def delete(self, request, pk=None):
        notification = self.get_object()
        if notification.recipient == request.user:
            notification.delete()
            data = {"success": True}
        else:
            data = {
                "success": False,
                "error": "You are not authorized to delete this notification.",
            }
        return Response(data)

    @action(detail=False, methods=["delete", "get"])
    def delete_all(self, request):
        Notification.objects.filter(recipient=request.user).delete()
        data = {"success": True}
        return Response(data)

    @action(detail=False, methods=["get"])
    def unread_count(self, request):
        count = Notification.objects.filter(recipient=request.user, unread=True).count()
        data = {"count": count}
        return Response(data)

    @action(detail=False, methods=["get"])
    def read_count(self, request):
        count = Notification.objects.filter(
            recipient=request.user, unread=False
        ).count()
        data = {"count": count}
        return Response(data)

    def get_queryset(self):
        return super().get_queryset().filter(recipient=self.request.user)

    def list(self, request):
        queryset = Notification.objects.filter(recipient=self.request.user)
        serializer = NotificationSerializer(queryset, many=True)
        return Response(serializer.data)
