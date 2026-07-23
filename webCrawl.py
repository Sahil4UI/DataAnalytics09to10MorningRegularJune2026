import urllib.request as url
import bs4
path = "https://indianexpress.com/"
response = url.urlopen(path)
data = bs4.BeautifulSoup(response)
newslist = data.find_all("h2",class_="topblockNews__sidebarTitle")
for news in newslist:
    print(news.text,end="\n\n")

# 