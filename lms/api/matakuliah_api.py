from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.pagination import PageNumberPagination, paginate

from ..models import MataKuliah
from .schemas import (
    MataKuliahSchema, MataKuliahCreateSchema, MataKuliahUpdateSchema
)

matakuliah_router = Router()

class MataKuliahPagination(PageNumberPagination):
    page_size = 10

@matakuliah_router.get("/", response=list[MataKuliahSchema])
@paginate(MataKuliahPagination)
def list_matakuliah(request, q: str | None = None):
    qs = MataKuliah.objects.all()
    if q:
        qs = qs.filter(nama_mk__icontains=q) | qs.filter(kode_mk__icontains=q)
    return qs

@matakuliah_router.get("/{int:id}", response=MataKuliahSchema)
def detail_matakuliah(request, id: int):
    return get_object_or_404(MataKuliah, id=id)

@matakuliah_router.post("/", response=MataKuliahSchema)
def create_matakuliah(request, data: MataKuliahCreateSchema):
    mk = MataKuliah.objects.create(
        kode_mk=data.kode_mk,
        nama_mk=data.nama_mk,
        sks=data.sks
    )
    return mk

@matakuliah_router.put("/{int:id}", response=MataKuliahSchema)
def update_matakuliah(request, id: int, data: MataKuliahUpdateSchema):
    mk = get_object_or_404(MataKuliah, id=id)
    if data.kode_mk is not None:
        mk.kode_mk = data.kode_mk
    if data.nama_mk is not None:
        mk.nama_mk = data.nama_mk
    if data.sks is not None:
        mk.sks = data.sks
    mk.save()
    return mk

@matakuliah_router.delete("/{int:id}")
def delete_matakuliah(request, id: int):
    mk = get_object_or_404(MataKuliah, id=id)
    mk.delete()
    return {"success": True}
