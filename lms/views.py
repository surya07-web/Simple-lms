from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import Mahasiswa, Nilai, MataKuliah, Kehadiran, SKS, Pengumuman, Tagihan, Jadwal


# ===============================
# 🌐 LANDING PAGE
# ===============================
def home(request):
    return render(request, 'home.html')


# ===============================
# 🔐 LOGIN / LOGOUT MAHASISWA
# ===============================
def login_mahasiswa(request):
    if request.method == 'POST':
        nim = request.POST.get('nim')
        nama = request.POST.get('nama')

        try:
            mahasiswa = Mahasiswa.objects.get(nim=nim, nama=nama)
            request.session['mahasiswa_id'] = mahasiswa.id  # Simpan sesi login
            messages.success(request, f"Selamat datang, {mahasiswa.nama}!")
            return redirect('dashboard_mahasiswa', nim=nim)
        except Mahasiswa.DoesNotExist:
            messages.error(request, "NIM atau Nama tidak ditemukan.")

    return render(request, 'mahasiswa/login.html')


def logout_user(request):
    if 'mahasiswa_id' in request.session:
        del request.session['mahasiswa_id']

    # 🔹 Bersihkan semua pesan lama
    storage = get_messages(request)
    for _ in storage:
        pass  # ini akan menghapus semua pesan yang belum ditampilkan

    messages.success(request, "Anda berhasil logout.")
    return redirect('login_mahasiswa')


# ===============================
# 🧑‍🎓 DASHBOARD MAHASISWA
# ===============================
def dashboard_mahasiswa(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    nilai_list = Nilai.objects.filter(mahasiswa=mahasiswa)

    menu = [
        {"label": "Kehadiran", "icon": "fa-solid fa-user-check", "color": "#22c55e"},
        {"label": "SKS", "icon": "fa-solid fa-book-open", "color": "#6366f1"},
        {"label": "Pengaturan", "icon": "fa-solid fa-gear", "color": "#9ca3af"},
        {"label": "Jadwal", "icon": "fa-solid fa-calendar-days", "color": "#facc15"},
        {"label": "Pengumuman", "icon": "fa-solid fa-bell", "color": "#E40A0A"},
        {"label": "Nilai", "icon": "fa-regular fa-star", "color": "#fb923c"},
    ]

    # 🔹 Ambil data pembayaran terbaru dari Tagihan
    tagihan_terbaru = Tagihan.objects.filter(mahasiswa=mahasiswa).order_by('-tanggal').first()

    if tagihan_terbaru:
        pembayaran = {
            "status": tagihan_terbaru.status,
            "jumlah": f"Rp {tagihan_terbaru.jumlah:,.0f}".replace(",", "."),
            "tanggal": tagihan_terbaru.tanggal.strftime("%d %B %Y"),
        }
    else:
        pembayaran = {
            "status": "Belum ada tagihan",
            "jumlah": "-",
            "tanggal": "-",
        }

    return render(request, 'mahasiswa/dashboard_mahasiswa.html', {
        'mahasiswa': mahasiswa,
        'nilai_list': nilai_list,
        'menu': menu,
        'pembayaran': pembayaran,
    })

# ===============================
# 📅 CRUD KEHADIRAN
# ===============================
def daftar_kehadiran(request):
    kehadiran_list = Kehadiran.objects.select_related('mahasiswa', 'mata_kuliah').all()
    return render(request, 'kehadiran/daftar.html', {'kehadiran_list': kehadiran_list})


def tambah_kehadiran(request):
    if request.method == 'POST':
        mahasiswa_id = request.POST.get('mahasiswa')
        mk_id = request.POST.get('mata_kuliah')
        tanggal = request.POST.get('tanggal')
        status = request.POST.get('status')

        mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
        mk = MataKuliah.objects.get(id=mk_id)

        Kehadiran.objects.create(
            mahasiswa=mahasiswa,
            mata_kuliah=mk,
            tanggal=tanggal,
            status=status
        )
        messages.success(request, "Data kehadiran berhasil ditambahkan!")
        return redirect('daftar_kehadiran')

    context = {
        'mahasiswa_list': Mahasiswa.objects.all(),
        'mk_list': MataKuliah.objects.all(),
    }
    return render(request, 'kehadiran/tambah.html', context)


def edit_kehadiran(request, id):
    kehadiran = get_object_or_404(Kehadiran, id=id)

    if request.method == 'POST':
        kehadiran.mahasiswa_id = request.POST.get('mahasiswa')
        kehadiran.mata_kuliah_id = request.POST.get('mata_kuliah')
        kehadiran.tanggal = request.POST.get('tanggal')
        kehadiran.status = request.POST.get('status')
        kehadiran.save()
        messages.success(request, "Data kehadiran berhasil diperbarui!")
        return redirect('daftar_kehadiran')

    context = {
        'kehadiran': kehadiran,
        'mahasiswa_list': Mahasiswa.objects.all(),
        'mk_list': MataKuliah.objects.all(),
    }
    return render(request, 'kehadiran/edit.html', context)


def hapus_kehadiran(request, id):
    kehadiran = get_object_or_404(Kehadiran, id=id)
    kehadiran.delete()
    messages.success(request, "Data kehadiran berhasil dihapus!")
    return redirect('daftar_kehadiran')


# ===============================
# 👨‍🎓 LIHAT KEHADIRAN (MAHASISWA)
# ===============================
def lihat_kehadiran(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    kehadiran_list = Kehadiran.objects.filter(mahasiswa=mahasiswa).select_related('mata_kuliah')

    return render(request, 'mahasiswa/kehadiran.html', {
        'mahasiswa': mahasiswa,
        'kehadiran_list': kehadiran_list
    })


# ===============================
# 🎓 LIHAT SKS (MAHASISWA)
# ===============================
def lihat_sks(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    data_sks = SKS.objects.filter(mahasiswa=mahasiswa)
    total_sks = sum(item.jumlah_sks for item in data_sks)

    return render(request, 'mahasiswa/lihat_sks.html', {
        'mahasiswa': mahasiswa,
        'data_sks': data_sks,
        'total_sks': total_sks,
    })


# ===============================
# ⚙️ PENGATURAN (MAHASISWA)
# ===============================
def pengaturan_mahasiswa(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    return render(request, 'mahasiswa/pengaturan.html', {'mahasiswa': mahasiswa})


def edit_profil_mahasiswa(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)

    if request.method == "POST":
        # hanya update field yang boleh diubah
        mahasiswa.alamat = request.POST.get("alamat", mahasiswa.alamat)

        if 'foto' in request.FILES:
            mahasiswa.foto = request.FILES['foto']

        mahasiswa.save()
        messages.success(request, "Profil berhasil diperbarui!")
        return redirect('pengaturan_mahasiswa', nim=mahasiswa.nim)

    # tampilkan halaman edit profil
    return render(request, 'mahasiswa/edit_profil_mahasiswa.html', {'mahasiswa': mahasiswa})


   

# ===============================
# 📅 LIHAT JADWAL (MAHASISWA)
# ===============================
def lihat_jadwal(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    # 🔥 Filter jadwal berdasarkan mahasiswa login
    jadwal_list = Jadwal.objects.filter(mahasiswa=mahasiswa).select_related('mata_kuliah', 'dosen')

    return render(request, 'mahasiswa/lihat_jadwal.html', {
        'mahasiswa': mahasiswa,
        'jadwal_list': jadwal_list,
    })

# ===============================
# 📅 PENGUMUMAN (MAHASISWA)
# ===============================
def daftar_pengumuman(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    pengumuman = Pengumuman.objects.all().order_by('-tanggal')
    return render(request, 'mahasiswa/pengumuman.html', {
        'mahasiswa': mahasiswa,
        'pengumuman': pengumuman
    })


# ===============================
# 📅 NILAI (MAHASISWA)
# ===============================
def lihat_nilai(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    nilai_list = Nilai.objects.filter(mahasiswa=mahasiswa).select_related('mata_kuliah')

    return render(request, 'mahasiswa/lihat_nilai.html', {
        'mahasiswa': mahasiswa,
        'nilai_list': nilai_list
    })

# ===============================
# 📅 TAGIHAN (MAHASISWA)
# ===============================
def lihat_tagihan(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    tagihan_list = Tagihan.objects.filter(mahasiswa=mahasiswa).order_by('-tanggal')
    return render(request, 'mahasiswa/lihat_tagihan.html', {
        'mahasiswa': mahasiswa,
        'tagihan_list': tagihan_list,
    })



# ===============================
# 📅 LIHAT PROFIL (MAHASISWA)
# ===============================
def lihat_profil(request, nim):
    mahasiswa = get_object_or_404(Mahasiswa, nim=nim)
    return render(request, 'mahasiswa/lihat_profil.html', {'mahasiswa': mahasiswa})

# ===============================
# 📋 CRUD MAHASISWA
# ===============================
def daftar_mahasiswa(request):
    data = []
    for mhs in Mahasiswa.objects.all():
        nilai = Nilai.objects.filter(mahasiswa=mhs)
        data.append({
            'mahasiswa': mhs,
            'nilai_list': nilai
        })
    return render(request, 'mahasiswa/daftar.html', {'data': data})


def tambah_mahasiswa(request):
    if request.method == 'POST':
        Mahasiswa.objects.create(
            nim=request.POST['nim'],
            nama=request.POST['nama'],
            prodi=request.POST['prodi'],
            angkatan=request.POST['angkatan']
        )
        messages.success(request, "Mahasiswa berhasil ditambahkan.")
        return redirect('daftar_mahasiswa')
    return render(request, 'mahasiswa/tambah.html')


def edit_mahasiswa(request, id):
    mahasiswa = get_object_or_404(Mahasiswa, id=id)
    if request.method == 'POST':
        mahasiswa.nim = request.POST['nim']
        mahasiswa.nama = request.POST['nama']
        mahasiswa.prodi = request.POST['prodi']
        mahasiswa.angkatan = request.POST['angkatan']
        mahasiswa.save()
        messages.success(request, "Data mahasiswa berhasil diperbarui.")
        return redirect('daftar_mahasiswa')
    return render(request, 'mahasiswa/edit.html', {'mahasiswa': mahasiswa})


def hapus_mahasiswa(request, id):
    mahasiswa = get_object_or_404(Mahasiswa, id=id)
    mahasiswa.delete()
    messages.success(request, "Data mahasiswa berhasil dihapus.")
    return redirect('daftar_mahasiswa')


# ===============================
# 📘 CRUD MATA KULIAH
# ===============================
def daftar_matakuliah(request):
    mk = MataKuliah.objects.all()
    return render(request, 'matakuliah/daftar.html', {'matakuliah_list': mk})


def tambah_matakuliah(request):
    if request.method == 'POST':
        MataKuliah.objects.create(
            kode_mk=request.POST['kode_mk'],
            nama_mk=request.POST['nama_mk'],
            sks=request.POST['sks']
        )
        messages.success(request, "Mata kuliah berhasil ditambahkan.")
        return redirect('daftar_matakuliah')
    return render(request, 'matakuliah/tambah.html')


def edit_matakuliah(request, id):
    mk = get_object_or_404(MataKuliah, id=id)
    if request.method == 'POST':
        mk.kode_mk = request.POST['kode_mk']
        mk.nama_mk = request.POST['nama_mk']
        mk.sks = request.POST['sks']
        mk.save()
        messages.success(request, "Mata kuliah berhasil diperbarui.")
        return redirect('daftar_matakuliah')
    return render(request, 'matakuliah/edit.html', {'matakuliah': mk})


def hapus_matakuliah(request, id):
    mk = get_object_or_404(MataKuliah, id=id)
    mk.delete()
    messages.success(request, "Mata kuliah berhasil dihapus.")
    return redirect('daftar_matakuliah')
