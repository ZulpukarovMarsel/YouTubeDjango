from django.urls import include, path
from apps.videos.views import *
urlpatterns = [
    path('video/', VideoListView.as_view(), name='video_list_api'),
    path('video/<int:id>/', VideoDetailView.as_view(), name='video_detail_api')
]
