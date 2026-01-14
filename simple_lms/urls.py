from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from lms.api.router import api
from django.conf.urls.static import static

urlpatterns = [
    # 🧩 Admin Django (dengan Jazzmin theme otomatis aktif)
    path('admin/', admin.site.urls),

    # 📊 Profiling menggunakan Django Silk
    path('silk/', include('silk.urls', namespace='silk')),

    # 🎓 Routing ke aplikasi utama (LMS)
    path('', include('lms.urls')),

    path("api/", api.urls),
]

# ✅ Agar file statis tetap bisa diakses saat DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ✅ Agar foto profil (media) bisa diakses
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
