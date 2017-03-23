# from app import db
# from flask_sqlalchemy import SQLAlchemy 
# from datetime import datetime, date
from bs4 import BeautifulSoup as bs
import requests
import feedparser
import html5lib
import re
import csv


# wiki_url = 'https://en.wikipedia.org/w/api.php?action=query&titles='+title+'&prop=revisions&rvprop=content&format=json'


def make_test_csv(url):


	content = requests.get(url).content

	soup = bs(content,'lxml')
	# print('========================================================================================================================')
	body = soup.find('div',{'id':'mw-content-text'})
	text=body.get_text().lower()

	clean_text=re.sub('[^a-z\ \']+'," ", text)
	# print(clean_text)
	words = list(clean_text.split())
	print(words)
	# print(words)
	with open('test.csv', "a") as output:
	    writer = csv.writer(output, lineterminator='\n')
	    writer.writerow(words)
	output.close() 

make_test_csv("https://en.wikipedia.org/wiki/Pascal%27s_theorem")