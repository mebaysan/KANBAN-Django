import os
from kanban.settings import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bvol9i&ktzt9a60@x&1j(z=%+_es28+p^+4*acs4_3v8=@$s7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

BASE_URL = 'http://127.0.0.1:8000' # şifremi unuttum vb viewlar için yaptığımız yöntem

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""
mail  =  kanbandjangoopensource@gmail.com
şifre =  kanbandjangoopensourcesifre
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # hangi mail uygulaması
EMAIL_HOST = 'smtp.gmail.com' # hangi mail servisi
EMAIL_HOST_USER = 'kanbandjangoopensource@gmail.com' # servise girilecek kullanıcı adı
EMAIL_HOST_PASSWORD = 'kanbandjangoopensourcesifre' # servise girilecek şifre
EMAIL_PORT = 587 # servis hangi portu kullanıyor
EMAIL_USE_TLS = True # şifreleme
