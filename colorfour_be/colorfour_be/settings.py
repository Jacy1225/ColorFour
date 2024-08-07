from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Line Login 
LINE_LOGIN_CHANNEL_ID = os.getenv('LINE_LOGIN_CHANNEL_ID')
LINE_LOGIN_CHANNEL_SECRET = os.getenv('LINE_LOGIN_CHANNEL_SECRET')

# Line Messaging API 
LINE_MESSAGING_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_MESSAGING_CHANNEL_ACCESS_TOKEN')
LINE_MESSAGING_CHANNEL_SECRET = os.getenv('LINE_MESSAGING_CHANNEL_SECRET')

# Google Login
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_LOGIN_CALLBACK_URL = os.getenv('GOOGLE_LOGIN_CALLBACK_URL')

FRONTEND_URL = os.getenv('FRONTEND_URL')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.line',
    'allauth.socialaccount.providers.google',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    'color_analyzer',
    'wardrobe_manager',
    'outfit_recommender',
    'shopping_advisor',
    'social_platform',
    'outfit_scheduler',
    'line',
    'authentication',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True

AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'allauth.account.auth_backends.AuthenticationBackend',
)

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
  ],
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',
  ],
}

DJOSER = {
  'LOGIN_FIELD': 'email',
  'SERIALIZERS': {},
}


SOCIALACCOUNT_PROVIDERS = {
  'line': {
    'APP': {
      'client_id':LINE_LOGIN_CHANNEL_ID,
      'secret': LINE_LOGIN_CHANNEL_SECRET
    },
    "SCOPE": {
      'profile',
      'openid',
      'email',
    }
  },
  'google': {
    'APP': {
      'client_id': os.getenv('GOOGLE_CLIENT_ID'),
      'secret': os.getenv('GOOGLE_CLIENT_SECRET'),
      'key': ''
    },
    'SCOPE': [
      'profile',
      'email',
    ],
    'AUTH_PARAMS': {
      'access_type': 'online',
    },
    'METHOD': 'oauth2',
    'VERIFIED_EMAIL': True,
    'CLIENT_CLASS': 'allauth.socialaccount.providers.oauth2.client.OAuth2Client',
  }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'colorfour_be.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'colorfour_be.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD" : os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-Hant"

TIME_ZONE = "Asia/Taipei"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]

# MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format': '{levelname} {asctime} {module} {message}',
      'style': '{',
    },
    'simple': {
      'format': '{levelname} {message}',
      'style': '{',
    },
  },
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'formatter': 'verbose',
    },
  },
  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': 'DEBUG',
      'propagate': True,
    },
    '': {
      'handlers': ['console'],
      'level': 'DEBUG',
    },
  },
}