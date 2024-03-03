from django.urls import include, path
from apps.videos.views import *
urlpatterns = [
    path('video/', VideosModelViewSet.as_view({'get': 'list'})),
    path('video/<int:pk>/', VideoModelViewSet.as_view({'get': 'retrieve'}))
]