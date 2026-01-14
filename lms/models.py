from django.db import models
from django.contrib.auth.models import User

# ===============================
# 👨‍🏫 Model Dosen
# ===============================
class Dosen(models.Model):
    nidn = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama} ({self.nidn})"

    class Meta:
        verbose_name = "Dosen"
        verbose_name_plural = "Dosen"


# ===============================
# 👨‍🎓 Model Mahasiswa
# ===============================
class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20, unique=True)
    prodi = models.CharField(max_length=100)
    angkatan = models.IntegerField()
    foto = models.ImageField(upload_to='mahasiswa/', blank=True, null=True)
    alamat = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "Mahasiswa"
        verbose_name_plural = "Mahasiswa"


# ===============================
# 📘 Model Mata Kuliah
# ===============================
class MataKuliah(models.Model):
    kode_mk = models.CharField(max_length=10)
    nama_mk = models.CharField(max_length=100)
    sks = models.IntegerField()

    def __str__(self):
        return f"{self.nama_mk} ({self.kode_mk})"

    class Meta:
        verbose_name = "Mata Kuliah"
        verbose_name_plural = "Mata Kuliah"


# ===============================
# 🧮 Model Nilai (DIPERBAIKI)
# ===============================
class Nilai(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)  # ✅ diperbaiki
    nilai = models.FloatField()

    def __str__(self):
        return f"{self.mahasiswa.nama} - {self.mata_kuliah.nama_mk} ({self.nilai})"

    class Meta:
        verbose_name = "Nilai"
        verbose_name_plural = "Nilai"


# ===============================
# 📅 Model Kehadiran
# ===============================
class Kehadiran(models.Model):
    STATUS_CHOICES = [
        ('Hadir', 'Hadir'),
        ('Izin', 'Izin'),
        ('Sakit', 'Sakit'),
        ('Alpa', 'Alpa'),
    ]

    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    tanggal = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.mahasiswa.nama} - {self.mata_kuliah.nama_mk} ({self.status})"

    class Meta:
        verbose_name = "Kehadiran"
        verbose_name_plural = "Kehadiran"


# ===============================
# 📢 Model Pengumuman
# ===============================
class Pengumuman(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tanggal = models.DateField(auto_now_add=True)
    penulis = models.CharField(max_length=100, default='Admin')

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name = "Pengumuman"
        verbose_name_plural = "Pengumuman"

# ===============================
# 📢 TAGIHAN
# ===============================
class Tagihan(models.Model):
    STATUS_CHOICES = [
        ('Lunas', 'Lunas'),
        ('Belum Lunas', 'Belum Lunas'),
    ]
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    nama_tagihan = models.CharField(max_length=100)
    jumlah = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Belum Lunas')
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.mahasiswa.nama} - {self.nama_tagihan} ({self.status})"
    
    class Meta:
        verbose_name = "Tagihan"
        verbose_name_plural = "Tagihan"

        
# ===============================
# 🗓️ Model Jadwal
# ===============================
class Jadwal(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    hari = models.CharField(max_length=20)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    ruangan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mata_kuliah.nama_mk} - {self.hari}"

    class Meta:
        verbose_name = "Jadwal"
        verbose_name_plural = "Jadwal"


# ===============================
# 🧾 Model SKS
# ===============================
class SKS(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey('MataKuliah', on_delete=models.CASCADE, related_name='sks_records')
    jumlah_sks = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        if self.mata_kuliah:
            self.jumlah_sks = self.mata_kuliah.sks
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.mahasiswa.nama} - {self.mata_kuliah.nama_mk} ({self.jumlah_sks} SKS)"

    class Meta:
        verbose_name = "SKS"
        verbose_name_plural = "SKS"
