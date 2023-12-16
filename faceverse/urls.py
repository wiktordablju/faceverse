from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('groups/', include('group_management.urls')),
    path('profile/', include('user_management.urls')),
    path('post_management', include('post_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
