from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.pagination import PageNumberPagination, paginate

from ..models import Pengumuman
from .schemas import (
    PengumumanSchema, PengumumanCreateSchema, PengumumanUpdateSchema
)

pengumuman_router = Router()

class PengumumanPagination(PageNumberPagination):
    page_size = 10

@pengumuman_router.get("/", response=list[PengumumanSchema])
@paginate(PengumumanPagination)
def list_pengumuman(request, q: str | None = None):
    qs = Pengumuman.objects.all().order_by('-tanggal')
    if q:
        qs = qs.filter(judul__icontains=q) | qs.filter(isi__icontains=q)
    return qs

@pengumuman_router.get("/{int:id}", response=PengumumanSchema)
def detail_pengumuman(request, id: int):
    return get_object_or_404(Pengumuman, id=id)

@pengumuman_router.post("/", response=PengumumanSchema)
def create_pengumuman(request, data: PengumumanCreateSchema):
    p = Pengumuman.objects.create(
        judul=data.judul,
        isi=data.isi,
        penulis=data.penulis
    )
    return p

@pengumuman_router.put("/{int:id}", response=PengumumanSchema)
def update_pengumuman(request, id: int, data: PengumumanUpdateSchema):
    p = get_object_or_404(Pengumuman, id=id)
    if data.judul is not None:
        p.judul = data.judul
    if data.isi is not None:
        p.isi = data.isi
    if data.penulis is not None:
        p.penulis = data.penulis
    p.save()
    return p

@pengumuman_router.delete("/{int:id}")
def delete_pengumuman(request, id: int):
    p = get_object_or_404(Pengumuman, id=id)
    p.delete()
    return {"success": True}
