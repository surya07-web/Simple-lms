from pathlib import Path
import os

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-test-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

# ✅ INSTALLED APPS (dengan Jazzmin untuk tampilan admin modern)
INSTALLED_APPS = [
    'jazzmin',  # 🎨 Tema modern untuk admin Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lms',   # aplikasi utama kamu
]

if DEBUG:
    INSTALLED_APPS += ['silk']

# ✅ MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # ✅ letakkan setelah SessionMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']
    
# URL & WSGI
ROOT_URLCONF = 'simple_lms.urls'
WSGI_APPLICATION = 'simple_lms.wsgi.application'

# ✅ TEMPLATE SETTINGS
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

# ✅ DATABASE SETTINGS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = []

# INTERNATIONALIZATION
LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# ✅ STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# DEFAULT PRIMARY KEY FIELD TYPE
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ SILK CONFIGURATION (Profiling)
SILKY_PYTHON_PROFILER = True
SILKY_AUTHENTICATION = True       # butuh login admin untuk akses /silk/
SILKY_AUTHORISATION = True
SILKY_ANALYZE_QUERIES = True

# ✅ JAZZMIN CUSTOMIZATION (Tampilan Admin)
JAZZMIN_SETTINGS = {
    "site_title": "Sistem LMS Mahasiswa",
    "site_header": "Panel Administrasi LMS",
    "site_brand": "LMS UDINUS",
    "welcome_sign": "Selamat datang di panel admin!",
    "copyright": "© 2025 Universitas Dian Nuswantoro",
    "search_model": "lms.Mahasiswa",
    "show_sidebar": True,
    "hide_apps": [],
    "order_with_respect_to": ["auth", "lms"],
}
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
