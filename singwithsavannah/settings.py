"""
Django settings for singwithsavannah project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from dev_utils.SiteLogger import * 
import dj_database_url
import logging
import socket
import os

# Setup a logger 
_LOGGER = create_logger(__name__, 'settings.log', FORMAT_1)

# Add Admins, will be emailed when debug is set to False 
ADMINS = [('John', 'johnmezzportfolio@gmail.com')]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ENVIRON = os.path.dirname(PROJECT_SRC)

_LOGGER.info('Current working directory : {}'.format(os.getcwd()))
_LOGGER.info('PROJECT_SRC DIRECTORY : {}'.format(PROJECT_SRC))
_LOGGER.info('PROJECT_SETTINGS_DIR DIRECTORY : {}'.format(PROJECT_SETTINGS_DIR))
_LOGGER.info('PROJCT_ENVIRON DIRECTORY: {}'.format(PROJECT_ENVIRON))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(n&3hk9#qi5g!1aj!w-x=(2j$ylra_ugy1+@_@4htvg=ie4b$4'

# SECURITY WARNING: don't run with debug turned on in production!
LOCAL_HOSTS = ['Macintosh.local']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

if hostname in LOCAL_HOSTS : 
    DEBUG=False
    ALLOWED_HOSTS=['127.0.0.1']
    _LOGGER.info('Debug has been set to {debug}'.format(debug=DEBUG))
    _LOGGER.info('Host name : {host}'.format(host=hostname))
   
else:
    DEBUG = False
    _LOGGER.info('Debug has been set to {debug}'.format(debug=DEBUG)) 
    _LOGGER.info('Host name : {host}'.format(host=hostname))
    _LOGGER.info('Host ip address : {ip}'.format(ip=ip_address))
    #attempting to use IP address of heroku server
    #ALLOWED_HOSTS = ['*.herokuapp.com', '*.com.herokudns.com', ip_address, 'singwithsavannah.herokuapp.com']
    ALLOWED_HOSTS = ['*.herokuapp.com', ip_address]
    # Need this for CSRF Token 
    CSRF_COOKIE_DOMAIN = '*.herokuapp.com'
    # ALLOWED_HOSTS = ['herokuapp.com', 'singwithsavannah.herokuapp.com', '.singwithsavannah.herokuapp.com', hostname, 
    # 'https://singwithsavannah.herokuapp.com/', 'www.singwithsavannah.herokuapp.com']
    _LOGGER.info('Using the following allowed hosts {0}'.format(ALLOWED_HOSTS))
    _LOGGER.info('CSRF_COOKIE_DOMAIN set to {0}'.format(CSRF_COOKIE_DOMAIN))

# Email setup
# Rememeber to unlock captcha
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sws_site',
    'blog',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'singwithsavannah.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_SRC, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'singwithsavannah.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_SRC, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

_LOGGER.info('db_from_env : {}'.format(db_from_env))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


# This is the input, where we input files, STATIC_ROOT is the output, where the files are moved to 
STATICFILES_DIRS = [
    os.path.join(PROJECT_SRC, 'static'),
]

# This is where static files are collected into 
STATIC_ROOT = os.path.join(PROJECT_ENVIRON, 'static_cdn')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_LOCATION = 'static'

# Static cdn the static root should live outside of the django project outside of src. This is because once the 
# static files are collected there, django shouldn't have any involvment with this directory.

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

