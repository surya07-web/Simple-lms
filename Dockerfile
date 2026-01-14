FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat untuk cek koneksi DB
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy semua project files
COPY . .

# Tambahkan script wait_for_db
COPY wait_for_db.sh /app/wait_for_db.sh
RUN chmod +x /app/wait_for_db.sh

# Expose Django default port
EXPOSE 8000

# Gunakan entrypoint agar menunggu DB dulu sebelum start Django
ENTRYPOINT ["/app/wait_for_db.sh"]

# Jalankan server Django setelah DB siap
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
