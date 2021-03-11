import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/top/"
response=requests.get(url)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")

baslıklar=soup.find_all("td",{"class":"titleColumn"})
reytingler=soup.find_all("td",{"class":"ratingColumn"})

for baslık,reyting in zip(baslıklar,reytingler):

    print("Baslık={}".format(baslıklar.text))
    print("Rayting={}".format(reytingler.text))

