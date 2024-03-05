from django.contrib import admin
from django.urls import path, include
from config.settings import base
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("apps.user.urls")),
    path("api/v1/", include("apps.videos.urls")),
]

if base.DEBUG:
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
