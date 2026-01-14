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

# ============================
# Pagination Class (BENAR)
# ============================
class MahasiswaPagination(PageNumberPagination):
    page_size = 5


# ============================
# LIST MAHASISWA
# ============================
@mahasiswa_router.get("/", response=list[MahasiswaSchema])
@paginate(MahasiswaPagination)
def list_mahasiswa(request, prodi: str = None, kelas: str = None, angkatan: int = None):
    qs = Mahasiswa.objects.all()
    if prodi: qs = qs.filter(prodi=prodi)
    if kelas: qs = qs.filter(kelas=kelas)
    if angkatan: qs = qs.filter(angkatan=angkatan)
    return qs


# ============================
# DETAIL MAHASISWA
# ============================
@mahasiswa_router.get("{nim}", response=MahasiswaSchema)
def detail_mahasiswa(request, nim: str):
    return get_object_or_404(Mahasiswa, nim=nim)


# ============================
# CREATE MAHASISWA
# ============================
@mahasiswa_router.post("/", response=MahasiswaSchema)
def create_mahasiswa(request, data: MahasiswaCreateSchema):
    m = Mahasiswa.objects.create(**data.dict())
    return m


# ============================
# UPDATE MAHASISWA
# ============================
@mahasiswa_router.put("{nim}", response=MahasiswaSchema)
def update_mahasiswa(request, nim: str, data: MahasiswaUpdateSchema):
    m = get_object_or_404(Mahasiswa, nim=nim)
    for field, value in data.dict().items():
        if value is not None:
            setattr(m, field, value)
    m.save()
    return m


# ============================
# UPLOAD FOTO
# ============================
@mahasiswa_router.post("{nim}/upload-foto", response=UploadFotoSchema)
def upload_foto(request, nim: str, file: UploadedFile = File(...)):
    m = get_object_or_404(Mahasiswa, nim=nim)
    m.foto.save(file.name, file)
    return {
        "message": "Foto berhasil diupload",
        "foto_url": request.build_absolute_uri(m.foto.url),
    }


# ============================
# DELETE MAHASISWA
# ============================
@mahasiswa_router.delete("{nim}")
def delete_mahasiswa(request, nim: str):
    m = get_object_or_404(Mahasiswa, nim=nim)
    m.delete()
    return {"success": True}
