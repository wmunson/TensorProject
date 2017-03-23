# from app import db
# from flask_sqlalchemy import SQLAlchemy 
# from datetime import datetime, date
from bs4 import BeautifulSoup as bs
from tflearn.data_utils import to_categorical, pad_sequences, VocabularyProcessor
import requests
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np

import tflearn
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
	count = len(words)
	print(words)
	# print(words)
	with open('test.csv', "w") as output:
	    writer = csv.writer(output, lineterminator='\n')
	    writer.writerow(words)
	output.close() 
	# print(count)
	return count

# make_test_csv("https://en.wikipedia.org/wiki/Pascal%27s_theorem")



def run_analysis():


	# dataframe = pd.Dataframe(X.values)
	# dataframe.columns
	df = pd.read_csv('tensor/train.csv', sep='|', names=['number'])
	testdf = pd.read_csv('test.csv', sep='|', names=['content'])
	# df[label] = df.A.str.split(',', n=1, expand=True)
	seed=testdf.content.tolist()
	seeddict = {0:seed}
	# print(seed)
	# print('dataframe')
	# print(df.number)
	df['num'] = df['number'].map(lambda x: x.split(',')[0])
	df['text'] = df['number'].map(lambda x: x.split(',')[1:])
	# print(df.num)
	num=[]
	text=[]
	for n in df['num']:
	  num.append(n)
	for t in df['text']:
	  text.append(t)

	d=dict(zip(num,text))
	text_len=len(df['text'])
	# print (d)

	# Fill null values with empty strings

	print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
	# print(type(df.num.apply(str)))
	# print(type(df.text))
	text = df['text'].astype(str)
	# num = df['num'].astype(str)
	# print(type(text))
	# print(text)

	# Extract the required columns for inputs and outputs
	totalX = text
	totalY = df.num

	# # Convert the strings in the input into integers corresponding to the dictionary positions
	# # Data is automatically padded so we need to pad_sequences manually
	vocab_proc = VocabularyProcessor(10)
	totalX = np.array(list(vocab_proc.fit_transform(totalX)))
	seed = np.array(list(vocab_proc.fit_transform(seed)))
	# # We will have 11 classes in total for prediction, indices from 0 to 10
	vocab_proc2 = VocabularyProcessor(1)
	totalY = np.array(list(vocab_proc2.fit_transform(totalY))) - 1
	# # Convert the indices into 11 dimensional vectors
	totalY = to_categorical(totalY, nb_classes=10)

	# Split into training and testing data
	# trainX, testX, trainY, testY = train_test_split(totalX, totalY, test_size=0.1)
	totalX = pad_sequences(totalX, maxlen=100, value=0.)
	seed = pad_sequences(seed, maxlen=100, value=0.)
	# testX = pad_sequences(testX, maxlen=100, value=0.)
	# print(trainX)
	# print(trainY)
	# print(testX)
	# print(testY)
	print('finshed tokenizing')

	net = tflearn.input_data([None,100])


	net = tflearn.embedding(net, input_dim=12000, output_dim=256)


	net = tflearn.lstm(net, 256, dropout=0.9, return_seq=True)

	net = tflearn.lstm(net, 256, dropout=0.9)
	net = tflearn.dropout(net, 0.5)
	# # The output is then sent to a fully connected layer that would give us our final 11 classes
	net = tflearn.fully_connected(net, 10, activation='softmax')
	# # We use the adam optimizer instead of standard SGD since it converges much faster
	net = tflearn.regression(net, optimizer='adam', learning_rate=0.001, loss='categorical_crossentropy')
	model = tflearn.DNN(net, tensorboard_verbose=0)
	print('starting fit')
	model.fit(totalX, totalY, validation_set=0.2, show_metric=True, batch_size=None, n_epoch=20)

	# model = tflearn.helpers.evaluator.Evaluator(model)
	result=model.predict_label(seed)[0][0]
	print(result)
	return result
	# model.save('model')
	#




	
