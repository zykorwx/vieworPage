#encoding:utf-8
# Django settings for vieworPage project.

# Identificando la ruta del proyecto
import os
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

DAJAXICE_MEDIA_PREFIX="dajaxice"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('zykor', 'enrique.wx@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'zykor$vieworPage',                      # Or path to database file if using sqlite3.
        'USER': 'zykor',                      # Not used with sqlite3.
        'PASSWORD': 'sandra12',                  # Not used with sqlite3.
        'HOST': 'mysql.server',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Mexico_City'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-Mx'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = os.path.join(RUTA_PROYECTO,'subidas')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(RUTA_PROYECTO,'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'cx0i)*oe@^h8zlm=3mvw3w&amp;l%+4%$!0hlmgr=k8c*-s9@uahf1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)


ROOT_URLCONF = 'vieworPage.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'vieworPage.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'disqus',
    'principal',
    'dajaxice',
    'dajax',
    'social_auth',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

DISQUS_API_KEY = 'kaJz3KB2ToQ9zh0VVCQkWCsD1OE2a6rJ6yjYHoShxxc9F4QeAFEDBPaWES0IVUP2'
DISQUS_WEBSITE_SHORTNAME = 'mangest'

# Registro y login configuraciones
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
    )
# Apis keys
TWITTER_CONSUMER_KEY         = 'CtfnQEbeggFbyqQRM53cw'
TWITTER_CONSUMER_SECRET      = 'THZhFvFMVN8iYPdVcLAT9Ig2AwvBrrQTLNjj8PJkD4'
FACEBOOK_APP_ID              = '306615159417586'
FACEBOOK_API_SECRET          = 'a0c086778c72d8fc8c57adfc3b850dde'
GOOGLE_OAUTH2_CLIENT_ID      = '156687870178.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'EfwPolT8ry4lCt7PfTrpUtSJ'

# Reconfigurando urls
LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

# Para que despues se cambien los urls
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

# nombre por default?
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

