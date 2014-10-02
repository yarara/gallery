"""
Django settings for gallery project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
djcelery.setup_loader()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v!b-n9i4a%a&pe-(=lw7p8+uiit6j#i=((m3pr3t@nnfhih@%z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'rest_framework',
    'galleryapp',
    #"djkombu",
    'kombu.transport.django',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gallery.urls'

WSGI_APPLICATION = 'gallery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gallery',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'gall',
        'PASSWORD': '12345678',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru'
DEFAULT_CHARSET = 'utf-8'
LANGUAGES = (
    ('ru', 'Russia'),
)

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)



STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
MANAGER_FROM_EMAIL = 'gallerytest@yandex.ru'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'gallerytest'
EMAIL_HOST_PASSWORD = 'Qwe123$'
EMAIL_PORT = 587

#STATICFILES_DIRS = ('/home/yaraat/project/gallery/gallery/files/static/',)
STATIC_ROOT = '/home/yaraat/project/gallery/gallery/files/static/'
STATIC_URL = '/static/'
MEDIA_URL  = '/media/'
MEDIA_ROOT = "/home/yaraat/project/gallery/gallery/files/media/"


#Celery
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
# BROKER_BACKEND = "djkombu.transport.DatabaseTransport"
# CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "yaraat"
BROKER_PASSWORD = "UG09sWLem"
BROKER_VHOST = "127.0.0.4:8000"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}