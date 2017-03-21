# import tflearn
# from tflearn.data_utils import to_categorical, pad_sequences
# from tflearn.datasets import imdb
# import pickle

# # obj =imdb.load_data(path='imdb.pkl',n_words=10000, valid_portion=0.1)
# # print((obj))
# # print(len(obj[1][1]))
# # print(len(obj[2][1]))

# with open('imdb.pkl','rb') as p:
# 	data = pickle.load(p)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print ((data))




import tflearn
from tflearn.data_utils import to_categorical, pad_sequences, VocabularyProcessor

from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np

load_model = 0
save_model = 0

# Select only the two columns we require. Game title and its corresponding emotion
# 
# dataframe = pd.Dataframe(X.values)
# dataframe.columns
df = pd.read_csv('train.csv', sep='|', names=['number'])

# df[label] = df.A.str.split(',', n=1, expand=True)

df['num'] = df['number'].map(lambda x: x.split(',')[0])
df['text'] = df['number'].map(lambda x: x.split(',')[1:])

# Fill null values with empty strings
print('dataframe')
print(df)
# dataframe.fillna(value='', inplace=True)
# dataframe['B'] = dataframe.A.str.split(',', n=1, expand=True)
# dataframe.B = dataframe.B.str.split(',')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
# print(type(df.num.apply(str)))
# print(type(df.text))
text = df['text'].astype(str)
# num = df['num'].astype(str)
# print(type(text))
# print(text)

# # Extract the required columns for inputs and outputs
totalX = text
totalY = df.num

# # Convert the strings in the input into integers corresponding to the dictionary positions
# # Data is automatically padded so we need to pad_sequences manually
vocab_proc = VocabularyProcessor(15)
totalX = np.array(list(vocab_proc.fit_transform(totalX)))

# # We will have 11 classes in total for prediction, indices from 0 to 10
vocab_proc2 = VocabularyProcessor(1)
totalY = np.array(list(vocab_proc2.fit_transform(totalY))) - 1
# # Convert the indices into 11 dimensional vectors
totalY = to_categorical(totalY, nb_classes=11)

# Split into training and testing data
trainX, testX, trainY, testY = train_test_split(totalX, totalY, test_size=0.1)
# trainX = pad_sequences(trainX, maxlen=100, value=0.)
# testX = pad_sequences(testX, maxlen=100, value=0.)
print(trainX)
print(trainY)
print(testX)
print(testY)
# # Build the network for classification
# # Each input has length of 15
net = tflearn.input_data([None, 15])
# # The 15 input word integers are then casted out into 256 dimensions each creating a word embedding.
# # We assume the dictionary has 10000 words maximum
net = tflearn.embedding(net, input_dim=10000, output_dim=256)
# # Each input would have a size of 15x256 and each of these 256 sized vectors are fed into the LSTM layer one at a time.
# # All the intermediate outputs are collected and then passed on to the second LSTM layer.
net = tflearn.lstm(net, 256, dropout=0.9, return_seq=True)
# # Using the intermediate outputs, we pass them to another LSTM layer and collect the final output only this time
net = tflearn.lstm(net, 256, dropout=0.9)
# # The output is then sent to a fully connected layer that would give us our final 11 classes
net = tflearn.fully_connected(net, 11, activation='softmax')
# # We use the adam optimizer instead of standard SGD since it converges much faster
net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
						 loss='categorical_crossentropy')

# # Train the network
model = tflearn.DNN(net, tensorboard_verbose=0)

if load_model == 1:
	model.load('gamemodel.tfl')

model.fit(trainX, trainY, validation_set=(testX, testY), show_metric=True, batch_size=32, n_epoch=20)

if save_model == 1:
	model.save('gamemodel.tfl')
	print ("Saved model!")