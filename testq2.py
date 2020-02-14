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

dicto = {
    1 : [r'(?P<letter>P|S)((?P<number>1|2|3))', '\g<number>\g<letter>'],
    2 : [r'\+{2,}', '+'],
    3 : [r'\s{2,}', " "],
    4 : [r'(?<=\d{1})-(?=\d+)', ""],
    5 : [r'\s+(?=_CIDADE|_ESTADO|_PAÍS)', ""],
    6 : [r'\s+(?=_\d{1}\w{1})', ""],
    7 : [r'(?<=\d{1}\w{1}_)', " "],
    8 : [r'\s+(?=\(+|\(-)', ""],
    9 : [r'(?<=(?i)não|nao) ', "_"],
    10 : [r'_(?=(?i)famoso|famosa)', "&"],
    11 : [r'(?<=[^\d\W]{1})\.|\.(?=[^\d\W]{1})-', ""],
    12 : [r'[^0-9]{0,1}\.(?=\d+)', " 0."]       
}


for keys in dicto: 
    print("replace", dicto[keys][1] + "isso")