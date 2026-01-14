from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 🌐 Halaman Utama
    path('', views.home, name='home'),

    # 🔐 Autentikasi Mahasiswa
    path('login_mahasiswa/', views.login_mahasiswa, name='login_mahasiswa'),
    path('logout/', views.logout_user, name='logout_user'),

    # 🧑‍🎓 Dashboard Mahasiswa
    path('mahasiswa/dashboard/<str:nim>/', views.dashboard_mahasiswa, name='dashboard_mahasiswa'),

    # 🧾 CRUD Mahasiswa (Admin)
    path('mahasiswa/', views.daftar_mahasiswa, name='daftar_mahasiswa'),
    path('mahasiswa/tambah/', views.tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/edit/<int:id>/', views.edit_mahasiswa, name='edit_mahasiswa'),
    path('mahasiswa/hapus/<int:id>/', views.hapus_mahasiswa, name='hapus_mahasiswa'),

    # 📘 CRUD Mata Kuliah (Admin)
    path('matakuliah/', views.daftar_matakuliah, name='daftar_matakuliah'),
    path('matakuliah/tambah/', views.tambah_matakuliah, name='tambah_matakuliah'),
    path('matakuliah/edit/<int:id>/', views.edit_matakuliah, name='edit_matakuliah'),
    path('matakuliah/hapus/<int:id>/', views.hapus_matakuliah, name='hapus_matakuliah'),

    # 🕒 CRUD Kehadiran (Admin)
    path('kehadiran/', views.daftar_kehadiran, name='daftar_kehadiran'),
    path('kehadiran/tambah/', views.tambah_kehadiran, name='tambah_kehadiran'),
    path('kehadiran/edit/<int:id>/', views.edit_kehadiran, name='edit_kehadiran'),
    path('kehadiran/hapus/<int:id>/', views.hapus_kehadiran, name='hapus_kehadiran'),

    # 👀 Tampilan Data Mahasiswa (User)
    path('mahasiswa/<str:nim>/kehadiran/', views.lihat_kehadiran, name='lihat_kehadiran'),
    path('mahasiswa/<str:nim>/sks/', views.lihat_sks, name='lihat_sks'),
    path('mahasiswa/<str:nim>/jadwal/', views.lihat_jadwal, name='lihat_jadwal'),

    # ⚙️ Pengaturan & Profil Mahasiswa
    path('mahasiswa/pengaturan/<str:nim>/', views.pengaturan_mahasiswa, name='pengaturan_mahasiswa'),
    path('mahasiswa/pengaturan/<str:nim>/edit/', views.edit_profil_mahasiswa, name='edit_profil_mahasiswa'),
    path('mahasiswa/<str:nim>/profil/', views.lihat_profil, name='lihat_profil'),

    # 📢 Menu Pengumuman
    path('mahasiswa/<str:nim>/pengumuman/', views.daftar_pengumuman, name='daftar_pengumuman'),

    # Lihat Nilai
    path('mahasiswa/<str:nim>/nilai/', views.lihat_nilai, name='lihat_nilai'),

    # Lihat Tagihan
    path('mahasiswa/<str:nim>/tagihan/', views.lihat_tagihan, name='lihat_tagihan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
