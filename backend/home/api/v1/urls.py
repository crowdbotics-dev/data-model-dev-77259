from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Test12ViewSet,Testing123ViewSet,Testing23ViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('test12', Test12ViewSet )
router.register('testing123', Testing123ViewSet )
router.register('testing23', Testing23ViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
