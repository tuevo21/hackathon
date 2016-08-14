from beautifulscraper import BeautifulScraper
import html5lib
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import image_scraper
import urllib3

items = ["bread", "butter", "eggs", "cereal", "beverage", "yogurt", "orangejuice", "applejuice"]

##method: retrieve_img: 
##Given [name], download all images from Bing search of [name] and put them in current directory

def retrieve_img(name):
	scraper=BeautifulScraper()
	url="http://www.bing.com/images/search?q=" + name + "&FORM=HDRSC2"
	body=scraper.go(url)
	text_url=body.find_all("a", class_="thumb")
	count=0
	for tag in text_url:
		#print url
		arr = str(tag).split(" ")
		#print arr
		for s in arr:
			if s[0:4]=="href":
				url=s[6:len(s)-1]
				connection_pool = urllib3.PoolManager()
				try:
					resp = connection_pool.request('GET',url )
					f = "train_data/" + open(name + str(count)+".jpg", 'wb')
					f.write(resp.data)
					f.close()
					resp.release_conn()
					print (name + " " +str(count))
					count=count+1
				except ValueError:
					print "Error"

for item in items:
	retrieve_img(item)

