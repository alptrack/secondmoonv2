"""
Django settings for slapnotes project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, json, django_filters

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
key = os.path.join(BASE_DIR, "secrets.json")
with open(key) as f:
    secrets = json.loads(f.read())

def get_secret(settings, secrets=secrets):
    try:
        return secrets[settings]
    except KeyError:
        error_msg = "Set the ***REMOVED***0***REMOVED*** environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webpack_loader',
    'notes.apps.NotesConfig',
    'knox',
    'rest_framework',
    'dynamic_preferences',
    'django_filters',
    'tinymce',
    # comment the following line if you don't want to use user preferences
    # 'dynamic_preferences.users.apps.UserPreferencesConfig',
]

REST_FRAMEWORK = ***REMOVED***
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
***REMOVED***

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'slapnotes.urls'

TEMPLATES = [
    ***REMOVED***
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': ***REMOVED***
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        ***REMOVED***,
    ***REMOVED***,
]

WSGI_APPLICATION = 'slapnotes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = ***REMOVED***
    'default': ***REMOVED***
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    ***REMOVED***
***REMOVED***


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    ***REMOVED***
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    ***REMOVED***,
    ***REMOVED***
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    ***REMOVED***,
    ***REMOVED***
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    ***REMOVED***,
    ***REMOVED***
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    ***REMOVED***,
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#TINYMCE_JS_URL = "https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.0.0/tinymce.min.js"
TINYMCE_DEFAULT_CONFIG = ***REMOVED***
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
***REMOVED***
TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = True

WEBPACK_LOADER = ***REMOVED***
    'DEFAULT': ***REMOVED***
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, '../webpack-stats.dev.json'),
    ***REMOVED***
***REMOVED***

REST_FRAMEWORK = ***REMOVED***
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'PAGE_SIZE': 1,
***REMOVED***

EMAIL_HOST = 'mail.gandi.net'
EMAIL_PORT = 25 
EMAIL_HOST_USER = 'slapnote-admin@slaponic.us'
DEFAULT_FROM_EMAIL = 'slapnote-admin@slaponic.us'
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")

#ReCAPTCHA
GOOGLE_RECAPTCHA_SECRET_KEY = get_secret("GOOGLE_RECAPTCHA_SECRET_KEY")
