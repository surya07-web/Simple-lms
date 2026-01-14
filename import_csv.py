import os
import django

# Setup environment Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_lms.settings')
django.setup()

import csv
from lms.models import Mahasiswa

with open('mahasiswa.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Mahasiswa.objects.create(
            nim=row['nim'],
            nama=row['nama'],
            prodi=row['prodi'],
            angkatan=row['angkatan']
        )

print("✅ Import data mahasiswa selesai!")
