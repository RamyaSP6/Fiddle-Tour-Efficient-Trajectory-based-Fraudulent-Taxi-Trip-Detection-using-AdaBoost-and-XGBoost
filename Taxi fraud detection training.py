import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
nltk.download('punkt')
import tflearn
import os
import subprocess
import numpy
import random
import json
import pickle
from time import sleep
from sklearn.neighbors import KNeighborsClassifier

with open("taxi.json") as file:
    data = json.load(file)
words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = numpy.array(training)
output = numpy.array(output)

with open("taxi.pickle", "wb") as f:
    pickle.dump((words, labels, training, output), f)
print('Training started')
print('Processing')
model1 = KNeighborsClassifier(n_neighbors=1)
model1.fit(training, output)
knnPickle = open('knnpickle_file', 'wb')
# source, destination 
pickle.dump(model1, knnPickle)
print('Training ended')
