from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from datetime import date, time

from .models import (
    Dosen, Mahasiswa, MataKuliah,
    Nilai, Kehadiran, Pengumuman,
    Tagihan, Jadwal, SKS
)


# ===============================
# Test Model Dosen
# ===============================
class DosenModelTest(TestCase):
    def test_create_dosen(self):
        dosen = Dosen.objects.create(
            nidn="123456",
            nama="Dr. Ajib",
            prodi="Informatika"
        )
        self.assertEqual(str(dosen), "Dr. Ajib (123456)")


# ===============================
# Test Model Mahasiswa
# ===============================
class MahasiswaModelTest(TestCase):
    def test_create_mahasiswa(self):
        mhs = Mahasiswa.objects.create(
            nama="Surya",
            nim="A11.2023.14902",
            prodi="Informatika",
            angkatan=2023
        )
        self.assertEqual(mhs.nim, "A11.2023.14902")


# ===============================
# Test Model Mata Kuliah
# ===============================
class MataKuliahModelTest(TestCase):
    def test_create_mata_kuliah(self):
        mk = MataKuliah.objects.create(
            kode_mk="IF123",
            nama_mk="Pemrograman Django",
            sks=3
        )
        self.assertEqual(str(mk), "Pemrograman Django (IF123)")


# ===============================
# Test Model Nilai
# ===============================
class NilaiModelTest(TestCase):
    def setUp(self):
        self.mhs = Mahasiswa.objects.create(
            nama="Surya",
            nim="A11.2023.14902",
            prodi="Informatika",
            angkatan=2023
        )
        self.mk = MataKuliah.objects.create(
            kode_mk="IF123",
            nama_mk="Pemrograman Django",
            sks=3
        )

    def test_create_nilai(self):
        nilai = Nilai.objects.create(
            mahasiswa=self.mhs,
            mata_kuliah=self.mk,
            nilai=90
        )
        self.assertEqual(nilai.nilai, 90)


# ===============================
# Test Model Kehadiran
# ===============================
class KehadiranModelTest(TestCase):
    def setUp(self):
        self.mhs = Mahasiswa.objects.create(
            nama="Surya",
            nim="A11.2023.14902",
            prodi="Informatika",
            angkatan=2023
        )
        self.mk = MataKuliah.objects.create(
            kode_mk="IF123",
            nama_mk="Basis Data",
            sks=3
        )

    def test_create_kehadiran(self):
        hadir = Kehadiran.objects.create(
            mahasiswa=self.mhs,
            mata_kuliah=self.mk,
            tanggal=date.today(),
            status="Hadir"
        )
        self.assertEqual(hadir.status, "Hadir")


# ===============================
# Test Model Pengumuman
# ===============================
class PengumumanModelTest(TestCase):
    def test_create_pengumuman(self):
        p = Pengumuman.objects.create(
            judul="UTS Dimulai",
            isi="UTS dimulai minggu depan",
            penulis="Admin"
        )
        self.assertEqual(str(p), "UTS Dimulai")


# ===============================
# Test Model Tagihan
# ===============================
class TagihanModelTest(TestCase):
    def setUp(self):
        self.mhs = Mahasiswa.objects.create(
            nama="Surya",
            nim="A11.2023.14902",
            prodi="Informatika",
            angkatan=2023
        )

    def test_create_tagihan(self):
        tagihan = Tagihan.objects.create(
            mahasiswa=self.mhs,
            nama_tagihan="SPP",
            jumlah=1500000,
            status="Belum Lunas"
        )
        self.assertEqual(tagihan.status, "Belum Lunas")


# ===============================
# Test Model Jadwal
# ===============================
class JadwalModelTest(TestCase):
    def setUp(self):
        self.mhs = Mahasiswa.objects.create(
            nama="Surya",
            nim="A11.2023.14902",
            prodi="Informatika",
            angkatan=2023
        )
        self.mk = MataKuliah.objects.create(
            kode_mk="IF123",
            nama_mk="OOP",
            sks=3
        )
        self.dosen = Dosen.objects.create(
            nidn="99999",
            nama="Pak Budi",
            prodi="Informatika"
        )

    def test_create_jadwal(self):
        jadwal = Jadwal.objects.create(
            mahasiswa=self.mhs,
            mata_kuliah=self.mk,
            dosen=self.dosen,
            hari="Senin",
            jam_mulai=time(8, 0),
            jam_selesai=time(10, 0),
            ruangan="H.3.4"
        )
        self.assertEqual(jadwal.hari, "Senin")


# ===============================
# Test Model SKS
# ===============================
class SKSModelTest(TestCase):
    def setUp(self):
        self.mhs = Mahasiswa.objects.create(
            nama="Surya",
            nim="A11.2023.14902",
            prodi="Informatika",
            angkatan=2023
        )
        self.mk = MataKuliah.objects.create(
            kode_mk="IF123",
            nama_mk="Struktur Data",
            sks=4
        )

    def test_sks_auto_fill(self):
        sks = SKS.objects.create(
            mahasiswa=self.mhs,
            mata_kuliah=self.mk
        )
        self.assertEqual(sks.jumlah_sks, 4)
