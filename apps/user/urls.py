from django.urls import path, include
from apps.user.views import SignUpAPIView, SignInAPIView
urlpatterns = [
    path('sign_up/', SignUpAPIView.as_view(), name='sign_up'),
    path('sign_in/', SignInAPIView.as_view(), name='sign_in'),
]
