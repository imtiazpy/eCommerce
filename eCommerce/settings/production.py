from .base import *

# DEBUG = env.bool("DEBUG", default=False)
DEBUG = os.environ['DEBUG']

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env.str("SECRET_KEY")
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['https://kurti-shop.herokuapp.com', '127.0.0.1']

try:
    from .local import *
except ImportError:
    pass
