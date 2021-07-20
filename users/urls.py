from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmailConfirmationAPIView, TokenAPI, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/email/", EmailConfirmationAPIView.as_view()),
    path("v1/auth/token/", TokenAPI.as_view()),
]
