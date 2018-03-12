import os

DEBUG = True
SECRET_KEY = os.urandom(24)
JWT_SECRET_KEY = os.urandom(24)
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access','refresh']
