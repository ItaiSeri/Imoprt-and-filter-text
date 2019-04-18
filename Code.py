import pandas as pd

dir = "C:/Users/ItaiSe/Downloads/"
FileName = 'BIֹ_TEENA.txt' 
FileDir =  dir + FileName

file = open(FileDir, mode='r')
text = file.read()
file.close()

WordList = []

for word in text.split():
    WordList.append(word)
 
Filtered = [',' + "\'" + word + "\'" for word in WordList if word[:3] == 'bi_']

FileDir_EXP =  dir + 'BIֹ_TEENA_EXP.txt' 

with open(FileDir_EXP,'w') as f:
    for word in Filtered:
        f.write("%s\n" % word)
