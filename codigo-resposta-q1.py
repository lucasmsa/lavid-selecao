import pandas as pd
import re

q1File = pd.read_csv('corpora/corpus-q1-v2.csv')

patternDict = {
    r'(?P<letter>P|S)((?P<number>1|2|3))': '\g<number>\g<letter>',
    r'\+{2,}': '+',
    r'\s{2,}': " ",
    r'(?<=\d{1})-(?=\d+)': "",
    r'\s+(?=_CIDADE|_ESTADO|_PAÍS)': "",
    r'\s+(?=_\d{1}\w{1})': "",
    r'(?<=\d{1}\w{1}_)': " ",
    r'\s+(?=\(+|\(-)': "",
    r'(?i)(?<=não|nao) ': "_",
    r'(?i)_(?=famoso|famosa)': "&",
    r'(?<=^\d\W{1})\.|\.(?=^\d\W{1})-': "",
    r'^0-9{0,1}\.(?=\d+)': " 0."
}


def replaceCSV(d, t):

    c = t[-2:]
    listLines = []
    
    for line in t:

        count = 0
        for key in d:
            count += 1
            line = re.sub(key, d[key], line)
            
        listLines.append(line)
    
    df[c.name] = listLines
     

df = pd.DataFrame()

replaceCSV(patternDict, q1File.gr)
replaceCSV(patternDict, q1File.gi)

df.to_csv('corpus-resposta/corpus-resposta-q1.csv')
