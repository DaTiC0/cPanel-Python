# Cpanel API
# TESTING 

from logging import error
from base64 import b64encode
import requests
import urllib.parse as uparse
import config

DEFAULT_USER_AGENT = config.DEFAULT_USER_AGENT

session = requests.session()
session.headers.update({'User-Agent': DEFAULT_USER_AGENT})


credentials = f'{config.USERNAME}:{config.PASSWORD}'
enc = b64encode(credentials.encode()).decode()
auth = f'Basic {enc}'
module = 'SSL'  # get module TEST
function = 'fetch_certificates_for_fqdns'  # get function TEST


base_url = '{}://{}:{}'.format('https', config.URL, config.PORT)
path = f'/execute/{module}/{function}'
params = ''
url = uparse.urljoin(base_url, path)
print(url)
headers = {'Authorization': auth}

r = session.post(url,headers=headers)

if r.status_code == 401:
    raise error
print(r.text)
