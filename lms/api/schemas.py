from ninja import Schema
from ninja import Schema, File
from ninja.files import UploadedFile

# ===========================
# Mahasiswa
# ===========================
class MahasiswaSchema(Schema):
    id: int
    nim: str
    nama: str
    prodi: str
    angkatan: int
    alamat: str | None = None

class MahasiswaCreateSchema(Schema):
    nim: str
    nama: str
    prodi: str
    angkatan: int
    alamat: str | None = None

class MahasiswaUpdateSchema(Schema):
    nama: str | None = None
    prodi: str | None = None
    angkatan: int | None = None
    alamat: str | None = None

class UploadFotoSchema(Schema):
    message: str
    foto_url: str

# ===========================
# Mata Kuliah
# ===========================
class MataKuliahSchema(Schema):
    id: int
    kode_mk: str
    nama_mk: str
    sks: int

class MataKuliahCreateSchema(Schema):
    kode_mk: str
    nama_mk: str
    sks: int

class MataKuliahUpdateSchema(Schema):
    kode_mk: str | None = None
    nama_mk: str | None = None
    sks: int | None = None

# ===========================
# Nilai
# ===========================
class NilaiSchema(Schema):
    id: int
    mahasiswa_id: int
    mata_kuliah_id: int
    nilai: float

class NilaiCreateSchema(Schema):
    mahasiswa_id: int
    mata_kuliah_id: int
    nilai: float

class NilaiUpdateSchema(Schema):
    nilai: float | None = None

# ===========================
# Kehadiran
# ===========================
class KehadiranSchema(Schema):
    id: int
    mahasiswa_id: int
    mata_kuliah_id: int
    tanggal: str
    status: str

class KehadiranCreateSchema(Schema):
    mahasiswa_id: int
    mata_kuliah_id: int
    tanggal: str
    status: str

class KehadiranUpdateSchema(Schema):
    tanggal: str | None = None
    status: str | None = None

# ===========================
# Pengumuman
# ===========================
class PengumumanSchema(Schema):
    id: int
    judul: str
    isi: str
    tanggal: str
    penulis: str

class PengumumanCreateSchema(Schema):
    judul: str
    isi: str
    penulis: str = "Admin"

class PengumumanUpdateSchema(Schema):
    judul: str | None = None
    isi: str | None = None
    penulis: str | None = None

# ===========================
# Tagihan
# ===========================
class TagihanSchema(Schema):
    id: int
    mahasiswa_id: int
    nama_tagihan: str
    jumlah: float
    status: str
    tanggal: str

class TagihanCreateSchema(Schema):
    mahasiswa_id: int
    nama_tagihan: str
    jumlah: float
    status: str = "Belum Lunas"

class TagihanUpdateSchema(Schema):
    status: str | None = None

# ===========================
# Jadwal
# ===========================
class JadwalSchema(Schema):
    id: int
    mahasiswa_id: int
    mata_kuliah_id: int
    dosen_id: int
    hari: str
    jam_mulai: str
    jam_selesai: str
    ruangan: str

class JadwalCreateSchema(Schema):
    mahasiswa_id: int
    mata_kuliah_id: int
    dosen_id: int
    hari: str
    jam_mulai: str
    jam_selesai: str
    ruangan: str

class JadwalUpdateSchema(Schema):
    hari: str | None = None
    jam_mulai: str | None = None
    jam_selesai: str | None = None
    ruangan: str | None = None
    
class UploadFotoSchema(Schema):
    message: str
    foto_url: str