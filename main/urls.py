from django.urls import path
from .views import *

urlpatterns = [
    path('video/', VideoList.as_view(), name='video-list'),
    path('video/<int:pk>/', VideoDetail.as_view(), name='video-detail'),
]
