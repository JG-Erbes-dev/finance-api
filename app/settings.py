from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-419t5i&xl)h4qqk)pq1z2q7h_0f1bin)d#b03*2yea)hxkiqpj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',

    'authentication',
    'corporateevents',
    'econdata',
    'financials',
    'marketdata',
    'search',
    'updatedata',
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

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
}


JAZZMIN_SETTINGS = {
    'site_title': 'Finance API',
    'site_header': 'Finance API',
    'site_brand': 'Finance API',

    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'corporateevents.BrStock': 'fas fa-arrow-trend-up',
        'corporateevents.UsStock': 'fas fa-flag-usa',
        'corporateevents.UsEtf': 'fas fa-circle-dollar-to-slot',
        'corporateevents.BrRealEstate': 'fas fa-industry',
        'econdata.CommodityPrice': 'fas fa-oil-well',
        'econdata.DollarExchangeRate': 'fas fa-dollar-sign',
        'econdata.CumulativeBrInflation': 'fas fa-money-bill-trend-up fa-flip-vertical',
        'econdata.BrInflation': 'fas fa-money-bill-trend-up fa-flip-vertical',
        'econdata.UsInflation': 'fas fa-money-bill-trend-up fa-flip-vertical',
        'econdata.BrInterestRate': 'fas fa-scale-balanced',
        'econdata.UsInterestRate': 'fas fa-scale-balanced',
        'marketdata.BrStock': 'fas fa-arrow-trend-up',
        'marketdata.UsStock': 'fas fa-flag-usa',
        'marketdata.Crypto': 'fas fa-bitcoin-sign',
        'marketdata.UsEtf': 'fas fa-circle-dollar-to-slot',
        'marketdata.BrRealEstate': 'fas fa-industry',
        'marketdata.BrTreasure': 'fas fa-building-columns',
        'search.BrStock': 'fas fa-server',
        'search.UsStock': 'fas fa-server',
        'search.Crypto': 'fas fa-server',
        'search.UsEtf': 'fas fa-server',
        'search.BrRealEstate': 'fas fa-server',
        'search.BrTreasure': 'fas fa-server',
    },

    'welcome_sign': 'Bem-vindo(a) à Finance API',

    'copyright': 'JG Solutions LTDA',

    'show_ui_builder': True,
}
