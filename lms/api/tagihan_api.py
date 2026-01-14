from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.pagination import PageNumberPagination, paginate

from ..models import Tagihan, Mahasiswa
from .schemas import (
    TagihanSchema, TagihanCreateSchema, TagihanUpdateSchema
)

tagihan_router = Router()

class TagihanPagination(PageNumberPagination):
    page_size = 10

@tagihan_router.get("/", response=list[TagihanSchema])
@paginate(TagihanPagination)
def list_tagihan(request, mahasiswa_id: int | None = None, status: str | None = None):
    qs = Tagihan.objects.select_related('mahasiswa').all().order_by('-tanggal')
    if mahasiswa_id:
        qs = qs.filter(mahasiswa_id=mahasiswa_id)
    if status:
        qs = qs.filter(status__iexact=status)
    return qs

@tagihan_router.get("/{int:id}", response=TagihanSchema)
def detail_tagihan(request, id: int):
    return get_object_or_404(Tagihan, id=id)

@tagihan_router.post("/", response=TagihanSchema)
def create_tagihan(request, data: TagihanCreateSchema):
    get_object_or_404(Mahasiswa, id=data.mahasiswa_id)
    t = Tagihan.objects.create(
        mahasiswa_id=data.mahasiswa_id,
        nama_tagihan=data.nama_tagihan,
        jumlah=data.jumlah,
        status=data.status
    )
    return t

@tagihan_router.put("/{int:id}", response=TagihanSchema)
def update_tagihan(request, id: int, data: TagihanUpdateSchema):
    t = get_object_or_404(Tagihan, id=id)
    if data.status is not None:
        t.status = data.status
        t.save()
    return t

@tagihan_router.delete("/{int:id}")
def delete_tagihan(request, id: int):
    t = get_object_or_404(Tagihan, id=id)
    t.delete()
    return {"success": True}
