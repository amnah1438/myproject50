from pathlib import Path
import os

# 🏗️ المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 المفتاح السري للمشروع (غيّريه عند النشر)
SECRET_KEY = 'django-insecure-4nrjl&6hxynae=1hk6r09*4y#%-*=dw#cju!#h87i70kvochmp'

# ⚙️ وضع التطوير (فعّلي False عند النشر)
DEBUG = True

ALLOWED_HOSTS = []

# 🧩 تعريف التطبيقات
INSTALLED_APPS = [
    # تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🌟 تطبيقات المشروع
    'core',
    'store',
    'billing',
]

# 🧱 الوسطاء (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ لدعم اللغة والترجمة
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔗 ملف روابط المشروع
ROOT_URLCONF = 'myproject50.urls'

# 🎨 إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',         # 📁 القوالب العامة
            BASE_DIR / 'core' / 'templates' # 📁 القوالب الخاصة بتطبيق core
        ],
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

# 🚀 تطبيق WSGI الرئيسي
WSGI_APPLICATION = 'myproject50.wsgi.application'

# 🗄️ إعداد قاعدة البيانات (SQLite الافتراضية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'         # اللغة العربية
TIME_ZONE = 'Asia/Riyadh'    # التوقيت المحلي (الرياض)
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 📂 إعداد الملفات الثابتة (Static Files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]   # مجلد التطوير
STATIC_ROOT = BASE_DIR / "staticfiles"     # مجلد الإنتاج

# 🖼️ إعداد ملفات الوسائط (Media Files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ⚙️ الإعداد الافتراضي للمفاتيح التلقائية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🌐 دعم ملفات الترجمة (Locale)
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
