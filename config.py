from os import environ, path
from dotenv import load_dotenv
# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


URL = environ.get('URL')
PORT = 2083
DEFAULT_USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0')
USERNAME = environ.get('USERNAME')
PASSWORD = environ.get('PASSWORD')