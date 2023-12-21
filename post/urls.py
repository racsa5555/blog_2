from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    # path('', include(router.urls)),
    path('', PostListCreateAPIView.as_view())
]
