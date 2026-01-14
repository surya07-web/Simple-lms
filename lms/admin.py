from django.contrib import admin
from .models import Mahasiswa, MataKuliah, Nilai, Kehadiran, SKS, Jadwal, Dosen, Pengumuman, Tagihan

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'prodi', 'angkatan')
    search_fields = ('nim', 'nama', 'prodi')

@admin.register(MataKuliah)
class MataKuliahAdmin(admin.ModelAdmin):
    list_display = ('kode_mk', 'nama_mk', 'sks')

@admin.register(Nilai)
class NilaiAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'mata_kuliah', 'nilai')
    list_filter = ('mata_kuliah',)

@admin.register(Kehadiran)
class KehadiranAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'mata_kuliah', 'tanggal', 'status')
    list_filter = ('status', 'mata_kuliah')
    search_fields = ('mahasiswa__nama', 'mata_kuliah__nama_mk')
    ordering = ('-tanggal',)

@admin.register(SKS)
class SKSAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'mata_kuliah', 'jumlah_sks')
    readonly_fields = ('jumlah_sks',)

@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
    list_display = ('mata_kuliah', 'dosen', 'hari', 'jam_mulai', 'jam_selesai', 'ruangan')
    list_filter = ('hari', 'ruangan')
    search_fields = ('mata_kuliah__nama_mk', 'dosen__nama', 'ruangan')
    ordering = ('hari', 'jam_mulai')

@admin.register(Dosen)
class DosenAdmin(admin.ModelAdmin):
    list_display = ('nidn', 'nama', 'prodi')
    search_fields = ('nidn', 'nama', 'prodi')

@admin.register(Pengumuman)
class PengumumanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis', 'tanggal')
    search_fields = ('judul', 'isi')
    ordering = ('-tanggal',)

# 🧾 Tambahan baru
@admin.register(Tagihan)
class TagihanAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'nama_tagihan', 'jumlah', 'status', 'tanggal')
    list_filter = ('status', 'tanggal')
    search_fields = ('mahasiswa__nama', 'nama_tagihan')
    ordering = ('-tanggal',)
