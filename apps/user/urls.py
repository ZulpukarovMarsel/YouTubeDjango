from django.urls import path, include
from apps.user.views import SignUpAPIView
urlpatterns = [
    path('sign_up/', SignUpAPIView.as_view(), name='sign_up'),
]
