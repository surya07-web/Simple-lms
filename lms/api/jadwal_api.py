from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.pagination import PageNumberPagination, paginate

from ..models import Jadwal, Mahasiswa, MataKuliah, Dosen
from .schemas import (
    JadwalSchema, JadwalCreateSchema, JadwalUpdateSchema
)

jadwal_router = Router()

class JadwalPagination(PageNumberPagination):
    page_size = 12

@jadwal_router.get("/", response=list[JadwalSchema])
@paginate(JadwalPagination)
def list_jadwal(request, mahasiswa_id: int | None = None, hari: str | None = None):
    qs = Jadwal.objects.select_related('mahasiswa', 'mata_kuliah', 'dosen').all()
    if mahasiswa_id:
        qs = qs.filter(mahasiswa_id=mahasiswa_id)
    if hari:
        qs = qs.filter(hari__iexact=hari)
    return qs

@jadwal_router.get("/{int:id}", response=JadwalSchema)
def detail_jadwal(request, id: int):
    return get_object_or_404(Jadwal, id=id)

@jadwal_router.post("/", response=JadwalSchema)
def create_jadwal(request, data: JadwalCreateSchema):
    get_object_or_404(Mahasiswa, id=data.mahasiswa_id)
    get_object_or_404(MataKuliah, id=data.mata_kuliah_id)
    get_object_or_404(Dosen, id=data.dosen_id)
    j = Jadwal.objects.create(
        mahasiswa_id=data.mahasiswa_id,
        mata_kuliah_id=data.mata_kuliah_id,
        dosen_id=data.dosen_id,
        hari=data.hari,
        jam_mulai=data.jam_mulai,
        jam_selesai=data.jam_selesai,
        ruangan=data.ruangan
    )
    return j

@jadwal_router.put("/{int:id}", response=JadwalSchema)
def update_jadwal(request, id: int, data: JadwalUpdateSchema):
    j = get_object_or_404(Jadwal, id=id)
    if data.hari is not None:
        j.hari = data.hari
    if data.jam_mulai is not None:
        j.jam_mulai = data.jam_mulai
    if data.jam_selesai is not None:
        j.jam_selesai = data.jam_selesai
    if data.ruangan is not None:
        j.ruangan = data.ruangan
    j.save()
    return j

@jadwal_router.delete("/{int:id}")
def delete_jadwal(request, id: int):
    j = get_object_or_404(Jadwal, id=id)
    j.delete()
    return {"success": True}
