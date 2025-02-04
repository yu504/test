"""
Django settings for visiontravel project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
from dj_database_url import parse as dburl
import environ
from google.cloud import vision


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Google Cloud Vision APIのサービスアカウント認証ファイルのパス
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
#GOOGLE_APPLICATION_CREDENTIALS = BASE_DIR / "C:/Users/y_ooba/Desktop/venv/vision-travel-project-448601-c4ca0fa7e25b.json"

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

"""
# render用
SUPERUSER_NAME = env("SUPERUSER_NAME")
SUPERUSER_EMAIL = env("SUPERUSER_EMAIL")
SUPERUSER_PASSWORD = env("SUPERUSER_PASSWORD")
"""

# Google Places APIのAPIキーを追加
GOOGLE_PLACES_API_KEY = "AIzaSyCaJee3wWa3zhI4Lumrg7qMFOKos4Ki_3g"

# Google Cloud Vision APIの認証ファイルパスを環境変数に設定
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(GOOGLE_APPLICATION_CREDENTIALS)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(((=cq!q329nyy_&cx2htqxwb_ve3*x%jyjgy^ac1fak!#@j*h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'certification',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'visiontravel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static')],
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

WSGI_APPLICATION = 'visiontravel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

default_dburl = "sqlite:///" + str(BASE_DIR / "db.sqlite3")

DATABASES = {
    "default": config("DATABASE_URL", default=default_dburl, cast=dburl),
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ja'

LANGUAGES = [
    ('ja', 'Japanese'),
    ('en', 'English'),
    ('fr', 'French'),
    ('es', 'Spanish'),
    ('zh', 'Chinese'),
]

LANGUAGE_SESSION_KEY = 'django_language'

LOCALE_PATHS = [
    BASE_DIR / 'locale',  # 翻訳ファイルの保存場所
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = str(BASE_DIR / "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# カスタムユーザーモデルを使用する場合
AUTH_USER_MODEL = 'user.CustomUser'

# ログイン後のリダイレクト先
LOGIN_REDIRECT_URL = 'mainmenu'
# ログアウト後のリダイレクト先
LOGOUT_REDIRECT_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # ここにSMTPサーバーのアドレスを設定
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

LOGIN_URL = '/user/login/'  # ログインURLの設定

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 3},  # 最低3文字に変更
    },
]