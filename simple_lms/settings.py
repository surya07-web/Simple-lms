from pathlib import Path
import os

# =========================
# BASE DIRECTORY
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# SECURITY
# =========================
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "simple-lms-production.up.railway.app",
    ".railway.app",
]

# =========================
# INSTALLED APPS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lms',
]

# Jazzmin & Silk hanya aktif di lokal (DEBUG=True)
if DEBUG:
    INSTALLED_APPS.insert(0, 'jazzmin')
    INSTALLED_APPS.append('silk')

# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ✅ wajib untuk Railway static
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE.insert(3, 'silk.middleware.SilkyMiddleware')

# =========================
# URL & WSGI
# =========================
ROOT_URLCONF = 'simple_lms.urls'
WSGI_APPLICATION = 'simple_lms.wsgi.application'

# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =========================
# DATABASE
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =========================
# PASSWORD
# =========================
AUTH_PASSWORD_VALIDATORS = []

# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# =========================
# STATIC & MEDIA
# =========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =========================
# DEFAULT PK
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# SILK CONFIG (HANYA DEBUG)
# =========================
if DEBUG:
    SILKY_PYTHON_PROFILER = True
    SILKY_AUTHENTICATION = True
    SILKY_AUTHORISATION = True
    SILKY_ANALYZE_QUERIES = True

# =========================
# JAZZMIN CONFIG (HANYA DEBUG)
# =========================
if DEBUG:
    JAZZMIN_SETTINGS = {
        "site_title": "Sistem LMS Mahasiswa",
        "site_header": "Panel Administrasi LMS",
        "site_brand": "LMS UDINUS",
        "welcome_sign": "Selamat datang di panel admin!",
        "copyright": "© 2025 Universitas Dian Nuswantoro",
        "search_model": "lms.Mahasiswa",
        "show_sidebar": True,
        "order_with_respect_to": ["auth", "lms"],
    }
