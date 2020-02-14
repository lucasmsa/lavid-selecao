import pandas as pd 
import re
import codecs
import json
from collections import OrderedDict

q2File = pd.read_csv('corpora/corpus-q2.csv')

wordsDict = {}
pattern = r'(?<!\[)\b[^\d\W]+\_{0,}\-{0,1}\w+\d{0,1}|\d{1}\w{1}_\w+_\d{1}\w{1}\b'

print('\n gr \n')

def wordCounter(d, t):

    for line in t:

        wordsFound = re.findall(pattern, line)

        for word in wordsFound:

            word = word.lower()
            
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

wordCounter(wordsDict, q2File.gr)
wordCounter(wordsDict, q2File.gi)

wordsDict = OrderedDict(sorted(wordsDict.items(), key= lambda col: -col[1]))

file = codecs.open("corpus-resposta/corpus-resposta-q2.json", "w", "utf-8")
json.dump(wordsDict, file, indent=4, sort_keys=False, ensure_ascii=False)
file.close()

print(wordsDict)