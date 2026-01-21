FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

ENV PYTHONUNBUFFERED=1

# Render pakai port 10000
EXPOSE 10000

# Jalankan migrate lalu gunicorn
CMD python manage.py migrate && gunicorn simple_lms.wsgi:application --bind 0.0.0.0:10000
