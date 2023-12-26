import os
from pathlib import Path

from django.contrib.messages import constants as messages
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




# yashirin kalit
SECRET_KEY = ')ce3afwgsvm@2*9to89xcd&=$22qxcz(cujim3$cm6$#*z2v)gb'

# DEBUG hamda hos sozlamari
DEBUG = False
ALLOWED_HOSTS = ['*']


# Application sozlamari

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # new
    'django.contrib.staticfiles',
    'coresite.apps.CoresiteConfig',   
    'accounts.apps.AccountsConfig',
    'courses.apps.CoursesConfig',
    'reviews.apps.ReviewsConfig',
    'carts.apps.CartsConfig',
    'billings.apps.BillingsConfig',
    'enrolls.apps.EnrollsConfig',
    'dashboard.apps.DashboardConfig',
    'customadmin.apps.CustomadminConfig',
    'quizapp.apps.QuizappConfig',
    'payment.apps.PaymentConfig',
    'star_ratings',
    'storages',
    'ckeditor',
]



# Midvarel sozlamari
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
      
]

ROOT_URLCONF = 'core.urls'







# templsates sozlamari
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # custom
                'coresite.context_processors.categories_context_processor',
                'coresite.context_processors.site_context_processor',

                # 3rd Party

            ],
        },

    },
]

WSGI_APPLICATION = 'core.wsgi.application'








# databaza sozlamalari 
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}











# tekshiruv yani autentificatsiya sozlamalari 
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


# vaqt mintaqa sozlamalari 

LANGUAGE_CODE = 'uz-uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True












# models sozlamalari
AUTH_USER_MODEL = 'accounts.CustomUser'


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}














# static sozlamalari
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]













# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'whitenoise.storage.ManifestStaticFilesStorage'
