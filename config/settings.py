import os

import dj_database_url
import environ
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if (os.getenv('DEBUG') == 'True') else False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'govuk_template_base',
    'govuk_forms',
    'gds_template',
    'user',
    'core',
    'kdashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.ProtectAllViewsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
                'govuk_template_base.context_processors.govuk_template_base',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'authbroker_client.backends.AuthbrokerBackend',
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

GOVUK_SERVICE_SETTINGS = {
    'name': 'Kibana Dashbard Access',
    'phase': 'alpha',
    #'header_link_view_name': 'staff_lookup',
}

#LOGIN_REDIRECT_URL = 'admin:index'
AUTH_USER_MODEL = 'user.User'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = 'login-redirect'
#LOGIN_REDIRECT_URL = 'admin-login-view'
LOGIN_URL = '/auth/login/'
AUTHBROKER_URL = os.getenv("AUTHBROKER_URL")
AUTHBROKER_CLIENT_ID = os.getenv("AUTHBROKER_CLIENT_ID")
AUTHBROKER_CLIENT_SECRET = os.getenv("AUTHBROKER_CLIENT_SECRET")
AUTHBROKER_SCOPES = "read write"
RESTRICT_ADMIN = env.bool("RESTRICT_ADMIN", True)

KIBANA_ADMIN_USER = os.getenv("KIBANA_ADMIN_USER")
KIBANA_ADMIN_PASSWORD = os.getenv("KIBANA_ADMIN_PASSWORD")
KIBANA_URL = os.getenv("KIBANA_URL")
MASTER_DASHBOARD_TOKEN = os.getenv("MASTER_DASHBOARD_TOKEN")
KIBANA_DOMAIN = os.getenv("KIBANA_DOMAIN")
ELASTIC_USER = os.getenv("ELASTIC_USER")
ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD")
ELASTIC_DOMAIN = os.getenv("ELASTIC_DOMAIN")
