 # import regular expressins packge
 # import numbers package
import numpy as np
import re

def readFile(fileName):
    file = open(fileName,'r',encoding="cp437")
    fileStr = ""
    for line in file:
        fileStr += line
    return fileStr
        
# Remove extra spaces
# Remove non-letter chars    
# Change to lower 
def preProcess(fileStr):
    fileStr = re.sub(" +"," ", fileStr)
    fileStr = re.sub("[^a-zA-Z ]","", fileStr)
    fileStr = fileStr.lower()
    return fileStr
            
rows = 5
fileContent = [""]*rows

#read  and preprocess files 
fileContent[0] = preProcess(readFile('DB.txt'))
fileContent[1] = preProcess(readFile('HP_small.txt'))
fileContent2 = preProcess(readFile('Tolkien.txt'))
fileContent3 = preProcess(readFile('Eliot.txt'))
numParts = 3
# split the third file to parts
partLength = int(len(fileContent2)/numParts) 
fileContent[2]  = fileContent2[0:partLength]
fileContent[3]  = fileContent2[partLength:partLength*2]
fileContent[4]  = fileContent2[partLength*2:partLength*3]
#___________________________________ 
# construct DICTIONARY concat files contents
numFiles = rows
allFilesStr = ""
for i in range(numFiles):
    allFilesStr += fileContent[i]

# generate a set of all words in files 
wordsSet =  set(allFilesStr.split())

# Read stop words file - words that can be removed
stopWordsSet = set(readFile('stopwords_en.txt').split())
# Remove the stop words from the word list
dictionary = wordsSet.difference(stopWordsSet)
#_______________________________________
# count the number of dictionary words in files
wordFrequency = np.empty((rows,len(dictionary)),dtype=np.int64)
for i in range(rows):
    for j,word in enumerate(dictionary):
        wordFrequency[i,j] = len(re.findall(word,fileContent[i]))
        
# find the distance matrix between the text files
dist = np.empty((rows,rows))
for i in range(rows): 
    for j in range(rows):
        # calculate the distance between the frequency vectors
        dist[i,j] = np.linalg.norm(wordFrequency[i,:]-wordFrequency[j,:])
        
print("dist=\n",dist)
        
# find the sum of the frequency colomns and select colomns having sum > 20
minSum = 20
sumArray =  wordFrequency.sum(axis=0)
indexArray = np.where(sumArray > minSum)
#independent work 1
wordFrequency2 = np.empty((rows,len(indexArray[0])),dtype=np.int64)
for i in range(rows):
    for j in range(len(indexArray[0])):
        wordFrequency2[i,j] = wordFrequency[i,indexArray[0][j]]
#end indpendent work 1

#indpendent work 2
dist2 = np.empty((rows,rows))
for i in range(rows):
    for j in range(rows):
        dist2[i,j] = np.linalg.norm(wordFrequency2[i,:]-wordFrequency2[j,:])

print("dist2=\n",dist2)
#end indpendent work 2

#independent work 3
rows2 = 6
fileContent4 = [""]*rows2
#split eliot.txt into parts
numParts2 = 2
partLength2 = int(len(fileContent3)/numParts2)
fileContent4[0] = fileContent3[0:partLength2]
fileContent4[1] = fileContent3[partLength2:partLength2*2]
#split tolkien.txt into parts
numParts3 = 4
partLength3 = int(len(fileContent2)/numParts3)
fileContent4[2] = fileContent2[0:partLength3]
fileContent4[3] = fileContent2[partLength3:partLength3*2]
fileContent4[4] = fileContent2[partLength3*2:partLength3*3]

numFiles2 = rows2
allFilesStr2 = ""
for i in range(numFiles2):
    allFilesStr2 += fileContent4[i]
wordsSet2 = set(allFilesStr2.split())
dictionary2 = wordsSet2.difference(stopWordsSet)
wordFrequency3 = np.empty((rows2,len(dictionary2)),dtype=np.int64)
for i in range(rows2):
    for j,word in enumerate(dictionary2):
        wordFrequency3[i,j] = len(re.findall(word, fileContent4[i]))
dist3 = np.empty((rows2,rows2))
for i in range(rows2):
    for j in range(rows2):
        dist3[i,j] = np.linalg.norm(wordFrequency3[i,:]-wordFrequency3[j,:])
print("dist3=\n",dist3)


