from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer
from .views import UserViewSet, activate_account, reset_password_confirm

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer),
        name="token_obtain_pair",
    ),
]

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
urlpatterns += router.urls

urlpatterns += [
    path(
        "activate-account/<str:uid>/<str:token>/",
        activate_account,
        name="activate-account",
    ),
    path(
        "password-reset-account/<str:uid>/<str:token>/",
        reset_password_confirm,
        name="reset-password",
    ),
]
