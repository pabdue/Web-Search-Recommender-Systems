#-------------------------------------------------------------------------
# AUTHOR: Pablo Duenas
# FILENAME: search_engine.py
# SPECIFICATION: 
# FOR: CS 4250- Assignment #1
# TIME SPENT: 
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])

#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}

for document in documents:
  index = documents.index(document)
  documents[index] = document.split(" ")

for document in documents:
  for term in document:
    if term in stopWords:
      document.remove(term)
# Output: [['love', 'cats', 'cats'], ['loves', 'dog'], ['love', 'dogs', 'cats']]

#Conduct stemming.
#--> add your Python code here
steeming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}
for document in documents:
  for term in document:
    index = document.index(term)
    if term in steeming.keys():
      term = steeming[term]
    document[index] = term
# Output: [['love', 'cat', 'cat'], ['love', 'dog'], ['love', 'dog', 'cat']]

#Identify the index terms.
#--> add your Python code here
terms = []
for document in documents:
    for term in document:
        if term not in terms:
            terms.append(term)

#Build the tf-idf term weights matrix.
#--> add your Python code here
docMatrix = []


#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []

#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here