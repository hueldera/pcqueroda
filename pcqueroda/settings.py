import os
import dynaconf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = dynaconf.DjangoDynaconf(__name__)  # noqa

