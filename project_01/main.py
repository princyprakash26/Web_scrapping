# Web scraping program

import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github user:')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')

profile_image = None
img_tag = soup.find('img', {'alt': 'Avatar'})
if img_tag is not None:
    profile_image = img_tag['src']

if profile_image is not None:
    print(profile_image)
else:
    print('Profile image not found.')
