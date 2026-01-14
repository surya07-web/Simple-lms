from ninja import Router, File
from ninja.files import UploadedFile
from ninja.pagination import PageNumberPagination, paginate
from django.shortcuts import get_object_or_404

from ..models import Mahasiswa
from .schemas import (
    MahasiswaSchema,
    MahasiswaCreateSchema,
    MahasiswaUpdateSchema,
    UploadFotoSchema
)

mahasiswa_router = Router()


# ============================================
# 📌 Pagination Class (Page size = 5)
# ============================================
class MahasiswaPagination(PageNumberPagination):
    page_size = 5


# ============================================
# 📌 LIST MAHASISWA (Pagination + Filter)
# GET /api/mahasiswa/
# ============================================
@mahasiswa_router.get("/", response=list[MahasiswaSchema])
@paginate(MahasiswaPagination)
def list_mahasiswa(request, prodi: str = None, angkatan: int = None):
    qs = Mahasiswa.objects.all()

    if prodi:
        qs = qs.filter(prodi=prodi)
    if angkatan:
        qs = qs.filter(angkatan=angkatan)

    return qs


# ============================================
# 📌 DETAIL MAHASISWA
# GET /api/mahasiswa/{nim}
# ============================================
@mahasiswa_router.get("/{nim}", response=MahasiswaSchema)
def detail_mahasiswa(request, nim: str):
    return get_object_or_404(Mahasiswa, nim=nim)


# ============================================
# 📌 CREATE MAHASISWA
# POST /api/mahasiswa/
# ============================================
@mahasiswa_router.post("/", response=MahasiswaSchema)
def create_mahasiswa(request, data: MahasiswaCreateSchema):
    mahasiswa = Mahasiswa.objects.create(
        nim=data.nim,
        nama=data.nama,
        prodi=data.prodi,
        angkatan=data.angkatan,
        alamat=data.alamat
    )
    return mahasiswa


# ============================================
# 📌 UPDATE MAHASISWA
# PUT /api/mahasiswa/{nim}
# ============================================
@mahasiswa_router.put("/{nim}", response=MahasiswaSchema)
def update_mahasiswa(request, nim: str, data: MahasiswaUpdateSchema):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)

    if data.nama is not None:
        mahasiswa.nama = data.nama
    if data.prodi is not None:
        mahasiswa.prodi = data.prodi
    if data.angkatan is not None:
        mahasiswa.angkatan = data.angkatan
    if data.alamat is not None:
        mahasiswa.alamat = data.alamat

    mahasiswa.save()
    return mahasiswa


# ============================================
# 📌 UPLOAD FOTO MAHASISWA
# POST /api/mahasiswa/{nim}/upload-foto
# ============================================
@mahasiswa_router.post("/{nim}/upload-foto", response=UploadFotoSchema)
def upload_foto(request, nim: str, file: UploadedFile = File(...)):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)

    mahasiswa.foto.save(file.name, file)

    return {
        "message": "Foto berhasil diupload",
        "foto_url": request.build_absolute_uri(mahasiswa.foto.url)
    }


# ============================================
# 📌 DELETE MAHASISWA
# DELETE /api/mahasiswa/{nim}
# ============================================
@mahasiswa_router.delete("/{nim}")
def delete_mahasiswa(request, nim: str):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    mahasiswa.delete()
    return {"success": True, "message": "Mahasiswa berhasil dihapus"}
