import os
from six import moves
import ssl

import tflearn
from tflearn.data_utils import *

path = "US_Cities.txt"
if not os.path.isfile(path):
    context = ssl._create_unverified_context()
    moves.urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt", path, context=context)

maxlen = 20

string_utf8 = open(path, "r").read().decode('utf-8')
X, Y, char_idx = \
    string_to_semi_redundant_sequences(string_utf8, seq_maxlen=maxlen, redun_step=3)

g = tflearn.input_data(shape=[None, maxlen, len(char_idx)])
g = tflearn.lstm(g, 512, return_seq=True)
g = tflearn.dropout(g, 0.5)
g = tflearn.lstm(g, 512)
g = tflearn.dropout(g, 0.5)
g = tflearn.fully_connected(g, len(char_idx), activation='softmax')
g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
                       learning_rate=0.001)

m = tflearn.SequenceGenerator(g, dictionary=char_idx,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,
                              checkpoint_path='model_us_cities')

for i in range(40):
    seed = random_sequence_from_string(string_utf8, maxlen)
    m.fit(X, Y, validation_set=0.1, batch_size=128,
          n_epoch=1, run_id='us_cities')
    print("-- TESTING...")
    print("-- Test with temperature of 1.2 --")
    print(m.generate(30, temperature=1.2, seq_seed=seed).encode('utf-8'))
    print("-- Test with temperature of 1.0 --")
    print(m.generate(30, temperature=1.0, seq_seed=seed).encode('utf-8'))
    print("-- Test with temperature of 0.5 --")
    print(m.generate(30, temperature=0.5, seq_seed=seed).encode('utf-8'))



#####################################################################################################################
################################################### model 

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
#   print (word)


# text = soup.get_text()
# print (text)
# b = body.replace('<a')

# body = soup.findAll('div',{'id':'bodyContent'})

# para = body.findAll('p')
# arr=[]
# for p in para:
#   # p.replace('<b>','')
#   # print(p)
#   arr.append(p)
# print(arr[0].content)
# with urlopen(url) as f:
#     document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())

#     
#############################################################################################
###################### tester 



