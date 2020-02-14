import re
import json
import codecs

wordsDict = {}
texts = []

text = 'EU ESTAR 22 POUCO BÊBADO [PONTO]'
text2 = '(-)BÊBADO [PONTO]'
text3 = 'maça da porra maçã maço'

texts.append(text)
texts.append(text2)
texts.append(text3)

pattern = r'(?<!\[)\b[^\d\W]+\_{0,}\d{0,1}|\d{1}\w{1}_\w+_\d{1}\w{1}\b'



for line in texts: 

    wordsFound = re.findall(pattern, line)

    for word in wordsFound:

        word = word.lower()
        
        if word not in wordsDict:
            wordsDict[word] = 1
        else:
            wordsDict[word] += 1

print(wordsDict)
 
file = codecs.open("blo.json", "w", "utf-8")
json.dump(wordsDict, file, indent=4, sort_keys=True, ensure_ascii=False)
file.close()