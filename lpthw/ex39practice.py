from bs4 import BeautifulSoup
import urllib2
wiki = "https://simple.wikipedia.org/wiki/List_of_United_States_cities_by_population"
header = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(wiki, headers =header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
print(soup)
'''area = ""
district = ""
town = ""
county = ""
table = soup.find("table", { "class" : "wikitable sortable" })
print table'''