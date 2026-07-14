import urllib.request as request

path = "https://timesofindia.indiatimes.com/"
response = request.urlopen(path)

import bs4
# BeautifulSoup4 - iska kaam hai data fetch krna
# pehle se ye python me installed nhi hota isko krna pdta hai following thse steps :
# open cmd
# pip install bs4
data = bs4.BeautifulSoup(response ,  features="html.parser")
newsList = data.find_all("div",class_="Kt6Pm style_change T5Q6J")
x=1
for news in newsList:
    print(x,"=>",news.text)
    print()
    x=x+1