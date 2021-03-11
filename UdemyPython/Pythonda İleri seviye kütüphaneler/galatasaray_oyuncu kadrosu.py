import requests
from bs4 import BeautifulSoup
url="https://www.galatasaray.org/pl/futbol-takim-kadrosu/9"
response=requests.get(url)
html_istegi=response.content
soup=BeautifulSoup(html_istegi,"html.parser")
takım_kadrosu=soup.find_all("div",{"class":"photolist_block"})
for takim in takım_kadrosu:
    print(takim.text)