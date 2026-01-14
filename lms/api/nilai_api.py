from ninja import Router
from django.shortcuts import get_object_or_404
from ninja.pagination import PageNumberPagination, paginate

from ..models import Nilai, Mahasiswa, MataKuliah
from .schemas import (
    NilaiSchema, NilaiCreateSchema, NilaiUpdateSchema
)

nilai_router = Router()

class NilaiPagination(PageNumberPagination):
    page_size = 10

@nilai_router.get("/", response=list[NilaiSchema])
@paginate(NilaiPagination)
def list_nilai(request, mahasiswa_id: int | None = None, mata_kuliah_id: int | None = None):
    qs = Nilai.objects.select_related('mahasiswa', 'mata_kuliah').all()
    if mahasiswa_id:
        qs = qs.filter(mahasiswa_id=mahasiswa_id)
    if mata_kuliah_id:
        qs = qs.filter(mata_kuliah_id=mata_kuliah_id)
    return qs

@nilai_router.get("/{int:id}", response=NilaiSchema)
def detail_nilai(request, id: int):
    return get_object_or_404(Nilai, id=id)

@nilai_router.post("/", response=NilaiSchema)
def create_nilai(request, data: NilaiCreateSchema):
    # validate existence
    get_object_or_404(Mahasiswa, id=data.mahasiswa_id)
    get_object_or_404(MataKuliah, id=data.mata_kuliah_id)
    n = Nilai.objects.create(
        mahasiswa_id=data.mahasiswa_id,
        mata_kuliah_id=data.mata_kuliah_id,
        nilai=data.nilai
    )
    return n

@nilai_router.put("/{int:id}", response=NilaiSchema)
def update_nilai(request, id: int, data: NilaiUpdateSchema):
    n = get_object_or_404(Nilai, id=id)
    if data.nilai is not None:
        n.nilai = data.nilai
        n.save()
    return n

@nilai_router.delete("/{int:id}")
def delete_nilai(request, id: int):
    n = get_object_or_404(Nilai, id=id)
    n.delete()
    return {"success": True}
