from django.urls import path, include
from social_django.views import auth as social_auth

urlpatterns = [
    # ...
    path('auth/', include('social_django.urls', namespace='social')),
    # Ваши другие URL-пути здесь
    # ...
]
