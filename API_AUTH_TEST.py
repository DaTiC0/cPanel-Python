
from logging import error
import requests
import urllib.parse as uparse
import config

# curl -H'Authorization: cpanel username:APITOKEN' 'https://example.com:2083/execute/Module/function?parameter=value'

session = requests.session()
session.headers.update({'User-Agent': config.DEFAULT_USER_AGENT})
credentials = f'{config.USERNAME}:{config.API}'
print(credentials)
headers = {
    'Authorization': f'cpanel {credentials}',
}
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

r = session.post(url, headers=headers, params=params)

if r.status_code == 401:
    raise error
try:
    print(r.json())
except ValueError:
    raise error

print(r.text)
