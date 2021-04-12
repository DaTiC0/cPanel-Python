
# from logging import error
import requests
import urllib.parse as uparse
import config

import logging

# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
try: # for Python 3
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
HTTPConnection.debuglevel = 1

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True



# curl -H'Authorization: cpanel username:APITOKEN' 'https://example.com:2083/execute/Module/function?parameter=value'

session = requests.session()

credentials = f'{config.USERNAME}:{config.API}'
headers = {
    'Authorization': f'cpanel {credentials}',
    'User-Agent': config.DEFAULT_USER_AGENT,
    'Accept': 'application/json'
}
session.headers.update(headers)

base_url = '{}://{}:{}'.format('https', config.URL, config.PORT)
module = 'Tokens'
function = 'list'
path = f'/execute/{module}/{function}'
url = uparse.urljoin(base_url, path)
print(url)


params = {}

r = session.post(url, params=params)

print(r.headers['Content-Type'])
print(r.status_code)

if r.status_code == 401:
    raise requests_log.error
try:
    print(r.json())
except ValueError:
    raise requests_log.error

print(r.text)
