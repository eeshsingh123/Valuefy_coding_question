#! Python 3.6 program to scrape the url : https://medium.com and gets links from all of its pages/
#! usage in README.MD
 
import re
from urllib.request import Request,urlopen
from multiprocessing import Pool

def scraper(u):
	try:
		req = Request(u, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read()
		webpage = str(webpage)

		#updated regex to find all the link elements with 'https://medium.com'
		my_urls = re.findall('http[s]?://medium\.com\/*[A-Za-z0-9-?@$%&#=_]*\/*[A-Za-z0-9-?@$%&#=_]*\/*[A-Za-z0-9-?@$%&#=_]*',webpage, flags=re.I) 

		# A set to hold all the unique links to avoid redundancy and save memory
		unique_links = set()

		#if url is already traversed then ignore it.
		#going through each and every url in the list for getting inner urls and calling it recursively. 
		for i in range(len(my_urls)):
			if my_urls[i] not in unique_links:
				with open('result.txt','a') as f:
					f.write(str(my_urls[i])+'\n')
			unique_links.add(my_urls[i]) 

		"""-----SOLUTION WITHOUT USING MULTIPROCESSING-----"""

		#recursively call the crawler to go through each url and return all the links
		# for i in list(unique_links):
		# 	if i!= u:                       #makes sure we do not get stuck in an infinite loop by traversing the same url again.
		# 		print(f'link:-> {i}')
		# 		scraper(str(i))

		"""-----SOLUTION USING MULTIPROCESSING-----"""

		#Using the Pool module for concurrency and multiprocessing
		ll = [i for i in list(unique_links) if i!= u]  #getting a list of only unique urls and not get stuck in infinite loop
		p = Pool(5) 					# 5 concurrent connections at a time
		res = p.map(scraper,ll)
		p.close()
		p.join()

	#Error handling in case of connection error or HTTP error or any Runtime error.
	except Exception as e:
		with open('Error_log.txt','a') as f:
			f.write(str(e)+'\n')
			return


if __name__ == '__main__':
	url = input('Enter the URL to crawl: ')
	scraper(url)
	# scraper('https://medium.com/')