"""
Django settings for agent project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

##########################################################################
## Imports
##########################################################################

import os
import warnings
import dj_database_url

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'
CONFDIR = Path(__file__).resolve()
PROJECT = CONFDIR.parent.parent


##########################################################################
## Path and Helpers
##########################################################################

def environ_setting(name, default=None, required=False):
    """
    Fetch setting from the environment or use the default. If required is set to True
    then a warning is raised that Django is not configured properly.
    """
    if name not in os.environ and required:
        warnings.warn(f"{name} ENVVAR is not set.", UserWarning)
        return default

    return os.environ.get(name, default)


def parse_bool(val):
    """
    Parse a boolean value from the environment; can set true, t, T, false, f, F, 0, 1
    """
    if isinstance(val, str):
        val = val.strip().lower()
        if val.startswith("f"):
            return False
        if val.startswith("t"):
            return True
        val = int(val)
    return bool(val)


##########################################################################
## Secrets
##########################################################################

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ_setting("SECRET_KEY", required=True)


##########################################################################
## Database
##########################################################################

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql_psycopg2"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


##########################################################################
## Runtime
##########################################################################

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = parse_bool(environ_setting("DJANGO_DEBUG", default=True))

# Specify hosts in production settings
ALLOWED_HOSTS = []
INTERNAL_IPS = ["127.0.0.1"]

# WSGI Configuration
ROOT_URLCONF = "agent.urls"
WSGI_APPLICATION = "agent.wsgi.application"

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Request Handling
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_TZ = True

##########################################################################
## Content (Static, Media, Templates)
##########################################################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = "static/"
STATICFILES_DIRS = (PROJECT / "static",)

# Media files (uploads)
MEDIA_URL = "uploads/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            PROJECT / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


##########################################################################
## Authentication
##########################################################################

LOGIN_URL = "/accounts/login/"
LOGIN_ERROR_URL = LOGIN_URL
LOGIN_REDIRECT_URL = "/"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
