from django.urls import path
from notifications.views import (
    live_all_notification_count,
    live_all_notification_list,
    live_unread_notification_count,
    live_unread_notification_list,
)
from rest_framework.routers import DefaultRouter

from .views import NotificationViewSet

router = DefaultRouter()
router.register(r"index", NotificationViewSet, basename="notification")
urlpatterns = router.urls
urlpatterns += [
    path("live-all-count/", live_all_notification_count),
    path("live-unread-count/", live_unread_notification_count),
    path("live-unread-list/", live_unread_notification_list),
    path("live-all-list/", live_all_notification_list),
]
