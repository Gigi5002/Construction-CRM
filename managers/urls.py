# managers/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet

router = DefaultRouter()
router.register(r'', ManagerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
