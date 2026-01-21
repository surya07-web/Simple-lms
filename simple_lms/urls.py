from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lms.urls')),
]

# 🔒 API Ninja (kalau ada)
try:
    from lms.api.router import api
    urlpatterns.append(path("api/", api.urls))
except:
    pass

# 🔒 SILK hanya aktif saat DEBUG=True
if settings.DEBUG:
    urlpatterns.append(
        path('silk/', include('silk.urls', namespace='silk'))
    )

# Static & media saat DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
