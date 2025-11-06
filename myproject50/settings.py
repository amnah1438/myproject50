from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-4nrjl&6hxynae=1hk6r09*4y#%-*=dw#cju!#h87i70kvochmp'

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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ لإضافة دعم الترجمة واللغة
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject50.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'myproject50.wsgi.application'

# 🗄️ قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 🌍 الإعدادات اللغوية والمنطقة الزمنية
LANGUAGE_CODE = 'ar'         # اللغة العربية
TIME_ZONE = 'Asia/Riyadh'    # التوقيت المحلي للرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 📁 الملفات الثابتة
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# 🔧 الإعداد الافتراضي للمفاتيح التلقائية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🌐 دعم الترجمات (إن احتجت لاحقًا)
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
