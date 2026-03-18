from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', include('users.urls')),
    path('', include('issues.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Dev-only: browser reload URL
if settings.DEBUG:
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
