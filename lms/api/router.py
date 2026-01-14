from ninja import NinjaAPI
from .mahasiswa_api import mahasiswa_router
from .matakuliah_api import matakuliah_router
from .nilai_api import nilai_router
from .kehadiran_api import kehadiran_router
from .pengumuman_api import pengumuman_router
from .tagihan_api import tagihan_router
from .jadwal_api import jadwal_router

api = NinjaAPI(
    title="API LMS",
    version="1.0.0",
    description="API untuk Sistem LMS"
)

api.add_router("/mahasiswa", mahasiswa_router, tags=["Mahasiswa"])
api.add_router("/matakuliah", matakuliah_router, tags=["MataKuliah"])
api.add_router("/nilai", nilai_router, tags=["Nilai"])
api.add_router("/kehadiran", kehadiran_router, tags=["Kehadiran"])
api.add_router("/pengumuman", pengumuman_router, tags=["Pengumuman"])
api.add_router("/tagihan", tagihan_router, tags=["Tagihan"])
api.add_router("/jadwal", jadwal_router, tags=["Jadwal"])
