#! Python 3.6 program to scrape the url : https://medium.com and gets links from all of its pages/
#! usage in README.MD

import sys, re
from urllib.request import Request,urlopen


def scraper(u):
	try:
		req = Request(u, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()
		webpage = str(webpage)

		# my_urls =  re.findall('"((http)s?://.*?)"', webpage)
		my_urls = re.findall('"((http)s?://.*?)"',webpage)

		#Write the url part of the tuple into result.txt file

		#going through each and every url in the tuple for getting inner urls and calling it recursively. 
		for i in range(5):
			with open('result.txt','a') as f:
				f.write(str(my_urls[i][0]))
			scraper(str(my_urls[i][0]))
			# print(str(my_urls[i][0]))1
			

	#Error handling in case of connection error or HTTP error
	except Exception as e:
		with open('Error_log.txt','a') as f:
			f.write(str(e))
			return

# url = input('Enter the URL to crawl: ')
# scraper(url)

scraper('https://medium.com/')
 




