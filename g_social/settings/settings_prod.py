from g_social.settings.settings import *

SECRET_KEY = os.environ.get("PROD_SECRET_KEY")
ALLOWED_HOSTS = ['django']
DEBUG = False
