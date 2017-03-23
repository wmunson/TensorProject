from bs4 import BeautifulSoup as bs
import requests
import feedparser
import html5lib
import re
import csv

import spacy
import pandas as pd


title = {'Apple':'5','Computer':'6','Tree':'5','Condensation':'5','Heat':'3','Paleolithic_diet':'3','Homeopathy':'3','Greco-Persian_Wars':'6','Wikipedia:List_of_really,_really,_really_stupid_article_ideas_that_you_really,_really,_really_should_not_create':'8','Ben_Going':'2'}
rows=[]
# labels = ['label','text']
# with open('train.csv', "a") as output:
# 	    writer = csv.writer(output, lineterminator='\n')
# 	    writer.writerow(labels)
# 	    output.close() 
for key, value in title.items():
	url = 'https://en.wikipedia.org/wiki/'+key

	content = requests.get(url).content

	soup = bs(content,'lxml')
	# print('========================================================================================================================')
	body = soup.find('div',{'id':'mw-content-text'})
	text=body.get_text().lower()

	clean_text=re.sub('[^a-z\ \']+'," ", text)
	# print(clean_text)
	words = list(clean_text.split())
	words.insert(0,value)
	print(words)
	# print(words)
	rows.append(words)

for row in rows:
	with open('train.csv', "a") as output:
	    writer = csv.writer(output, lineterminator='\n')
	    writer.writerow(row)
output.close() 

