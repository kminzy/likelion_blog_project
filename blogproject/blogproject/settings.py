"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-5$r*)irqa%o-t(t(5)8^99ll7%pxtusdubd=3&4b%--zi($ta_')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG', 'TRUE') != 'False')

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'account.CustomUser' #인증하는 유저 모델로 사용하겠다고 선언, 인증 관련 클래스/메소드들이 user model과 밀접한 관련


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'portfolio.apps.PortfolioConfig',
    'account.apps.AccountConfig',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['blogproject/templates'],
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

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : os.environ.get('DB_NAME'),
        'USER' : os.environ.get('DB_USER'),
        'PASSWORD' : os.environ.get('DB_PASSWORD'),
        'HOST' : os.environ.get('DB_HOST'),
        'PORT' : '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#유저에게 static파일 보여줄 때 가장 앞의 url
STATIC_URL = '/static/'

#현재 static 파일들이 어디에 있는지 경로 작성해줌
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blog', 'static'),
    os.path.join(BASE_DIR, 'portfolio', 'static'),
]



#static파일을 어디에 모을건지
#python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#유저가 업로드한 파일을 모으는 곳
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#유저에게 업로드한 파일 보여줄 때 가장 앞의 url
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#AWS
AWS_ACCESS_KEY_ID = 'AKIAXYJPRYP4VQHDU2VM'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'lion-bucket'
AWS_S3_SIGNATURE_VERSION= 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'
