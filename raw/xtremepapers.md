Title: Xtremepapers download script
status: draft

Here's a Python script I wrote to download past papers from [Xtremepapers.net][1].
You'll need to have [BeautifulSoup 4][2] to use it. Just replace the value in the "url" and run it to have all the PDF files in "

	::python
	from bs4 import BeautifulSoup 
	import requests 
	import urlparse
	from urllib import pathname2url
	import os
	url = "http://www.xtremepapers.com/CIE/index.php?dir=International%20A%20And%20AS%20Level/9231%20-%20Further%20Mathematics/"

	r = requests.get(url).text

	soup = BeautifulSoup(r)

	def construct_filename(file_url):
		q = urlparse.urlparse(file_url).query
		q_parsed = urlparse.parse_qs(q)
		download_link = 'http://www.xtremepapers.com/CIE/' + pathname2url(q_parsed['dir'][0]+ q_parsed['file'][0])
		#print download_link
		return download_link

	for link in soup.find_all('a', attrs={'class':'autoindex_a'}):
		if link.get('href')[-3:len(link.get('href'))] == 'pdf':
			file_url= 'http://www.xtremepapers.com/' + link.get('href')
			construct_filename(file_url)
			os.system('wget ' + construct_filename(file_url) )
