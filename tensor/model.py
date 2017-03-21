from bs4 import BeautifulSoup as bs
import requests
import feedparser
import html5lib
import re
import csv

import spacy
import pandas as pd


title = {'Apple':'0.5','Computer':'0.6','Tree':'0.4','Condensation':'0.5','Heat':'0.4'}
rows=[]
for key, value in title.items():
	url = 'https://en.wikipedia.org/wiki/'+key

	# wiki_url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json'


	content = requests.get(url).content

	soup = bs(content,'lxml')
	print('========================================================================================================================')
	body = soup.find('div',{'id':'mw-content-text'})
	text=body.get_text().lower()

	# pd.set_option('display.max_colwidth',-1)
	# nlp = spacy.load('en')

	# doc = nlp(text)
	# sentences = [sentence.orth_ for sentence in doc.sents]
	# print("There were {} sentences found.".format(len(sentences)))

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

# csvfile = open('train.csv', 'rb')
# csvwriter = csv.writer(csvfile)
# for item in words:
#     csvwriter.writerow(item.encode())
# csvfile.close()
# for word in text:
# 	print (word)


# text = soup.get_text()
# print (text)
# b = body.replace('<a')

# body = soup.findAll('div',{'id':'bodyContent'})

# para = body.findAll('p')
# arr=[]
# for p in para:
# 	# p.replace('<b>','')
# 	# print(p)
# 	arr.append(p)
# print(arr[0].content)
# with urlopen(url) as f:
#     document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())

#     