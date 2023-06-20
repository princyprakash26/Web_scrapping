# Web scraping program

import requests
from bs4 import BeautifulSoup as bs

class web_scrapping:
    def get_userprofile(self):
        githubuser = input('Enter your Github user name:')
        url = 'https://github.com/'+githubuser
        r = requests.get(url)
        soup = bs(r.content, 'html.parser')
        profile_image = soup.find('img',{'alt' : 'Avatar'})['src']
        return profile_image

image = web_scrapping()
print(image.get_userprofile())
