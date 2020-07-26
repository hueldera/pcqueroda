import os
import dynaconf
import django_heroku
from google.oauth2 import service_account

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


GS_BUCKET_NAME = 'pcqueroda-images'
GS_PROJECT_ID  = 'pcqueroda'

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    "images-website-gc-credentials.json"
)

settings = dynaconf.DjangoDynaconf(__name__)  # noqa

django_heroku.settings(locals())