from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("api/v1/notifications/", include("notification.urls")),
    path("api/v1/colleges/", include("colleges.urls")),
    path("api/v1/settings/", include("settings.urls")),
    path("api/v1/students/", include("students.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # API schema
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Invalid path
    re_path(r"^$", TemplateView.as_view(template_name="index.html")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
