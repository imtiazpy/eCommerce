from .base import *

DEBUG = env.bool("DEBUG", default=False)

try:
    from .local import *
except ImportError:
    pass
