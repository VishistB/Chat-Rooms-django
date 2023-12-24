# import os
# from .settings import *
# from .settings import BASE_DIR

# ALLOWED_HOSTS=[os.environ['WEBSITE_HOSTNAME']]
# CSRF_TRUSTED_ORIGINS=['https://'+os.environ['WEBSITE_HOSTNAME']]
# DEBUG = False


# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     'whitenoise.middleware.WhiteNoiseMiddleware'
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }