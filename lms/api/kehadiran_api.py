from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.pagination import PageNumberPagination, paginate

from ..models import Kehadiran, Mahasiswa, MataKuliah
from .schemas import (
    KehadiranSchema, KehadiranCreateSchema, KehadiranUpdateSchema
)

kehadiran_router = Router()

class KehadiranPagination(PageNumberPagination):
    page_size = 15

@kehadiran_router.get("/", response=list[KehadiranSchema])
@paginate(KehadiranPagination)
def list_kehadiran(request, mahasiswa_id: int | None = None, mata_kuliah_id: int | None = None):
    qs = Kehadiran.objects.select_related('mahasiswa', 'mata_kuliah').all()
    if mahasiswa_id:
        qs = qs.filter(mahasiswa_id=mahasiswa_id)
    if mata_kuliah_id:
        qs = qs.filter(mata_kuliah_id=mata_kuliah_id)
    return qs

@kehadiran_router.get("/{int:id}", response=KehadiranSchema)
def detail_kehadiran(request, id: int):
    return get_object_or_404(Kehadiran, id=id)

@kehadiran_router.post("/", response=KehadiranSchema)
def create_kehadiran(request, data: KehadiranCreateSchema):
    get_object_or_404(Mahasiswa, id=data.mahasiswa_id)
    get_object_or_404(MataKuliah, id=data.mata_kuliah_id)
    k = Kehadiran.objects.create(
        mahasiswa_id=data.mahasiswa_id,
        mata_kuliah_id=data.mata_kuliah_id,
        tanggal=data.tanggal,
        status=data.status
    )
    return k

@kehadiran_router.put("/{int:id}", response=KehadiranSchema)
def update_kehadiran(request, id: int, data: KehadiranUpdateSchema):
    k = get_object_or_404(Kehadiran, id=id)
    if data.tanggal is not None:
        k.tanggal = data.tanggal
    if data.status is not None:
        k.status = data.status
    k.save()
    return k

@kehadiran_router.delete("/{int:id}")
def delete_kehadiran(request, id: int):
    k = get_object_or_404(Kehadiran, id=id)
    k.delete()
    return {"success": True}
