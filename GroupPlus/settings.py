"""
Django settings for GroupPlus project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from os import urandom
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '9)v&g2uaenrq9jl*!ovznwpyj@ti&mn+l^k8&lx4z79@6t)chi')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    os.environ.get('ALLOWED_HOST', "")
]

# Application definition

INSTALLED_APPS = [
    'groups.apps.GroupsConfig',
    'verify.apps.VerifyConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_apscheduler'
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'GroupPlus.urls'

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

WSGI_APPLICATION = 'GroupPlus.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sjtu-plus',
        'USER': 'sjtu-plus',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': 'postgres-db',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/data/'

GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', '')

GITHUB_PERSONAL_ACCESS_TOKEN = os.environ.get('GITHUB_PERSONAL_ACCESS_TOKEN', '')

GITHUB_TRIGGER_URL = 'https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches'.format(
    owner='sjtu-plus',
    repo='sjtu-plus.github.io',
    workflow_id='2177133'
)

DEPLOYMENT_INTERVAL = 60

JACCOUNT_CLIENT_ID = os.environ.get('JACCOUNT_CLIENT_ID', '')

JACCOUNT_CLIENT_SECRET = os.environ.get('JACCOUNT_CLIENT_SECRET', '')

ATTESTATION_SECRET = os.environ.get('ATTESTATION_SECRET', '')
