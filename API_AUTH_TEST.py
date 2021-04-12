
from logging import error
import requests
import urllib.parse as uparse
import config

# curl -H'Authorization: cpanel username:APITOKEN' 'https://example.com:2083/execute/Module/function?parameter=value'

session = requests.session()

credentials = f'{config.USERNAME}:{config.API}'
headers = {
    'Authorization': f'cpanel {credentials}',
    'User-Agent': config.DEFAULT_USER_AGENT
}
session.headers.update(headers)

base_url = '{}://{}:{}'.format('https', config.URL, config.PORT)
module = 'SSL'
function = 'fetch_certificates_for_fqdns'
path = f'/execute/{module}/{function}'
url = uparse.urljoin(base_url, path)
print(url)

domain = input('Enter domain to get SSL:')
params = {
    'domains': domain
}

r = session.post(url, params=params)

print(r.headers['Content-Type'])
print(r.status_code)

if r.status_code == 401:
    raise error
try:
    print(r.json())
except ValueError:
    raise error

print(r.text)
