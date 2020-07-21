import os
import dynaconf
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = dynaconf.DjangoDynaconf(__name__)  # noqa

django_heroku.settings(locals())