from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request 
site= "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring.html"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = Request(site, headers=hdr)
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")
soup.find("a",{"class":"more downloadLink InternalLink"})
dl_link=r"https://rki.de"+soup.find("a",{"class":"more downloadLink InternalLink"})['href']
date=soup.find("a",{"class":"more downloadLink InternalLink"})['title'].split('(')[1].split(',')[0]
print(dl_link)
print(date)
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
path='impf'+"\\"+f"{date}.xlsx"
urllib.request.urlretrieve(dl_link, path)