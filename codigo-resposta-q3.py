import re 
import pandas as pd

f = open("corpus-resposta/corpus-resposta-q3.txt", "w")
q3File = pd.read_csv('corpora/corpus-q3.csv')

def augmentLines(file, t):
    
    pattern = r'\d{1}\w{1}_\w+R_\d{1}\w{1}'

    for line in t:
        verb = re.search(pattern, line)

        if verb == None:
            pass

        else: 

            newFlex = verb.group(0).split('_')
            letterF = 'S'
            letterS = 'S'

            for p in range(1, 3, 1):
                if p == 2:
                    letterF = 'P'
                for i in range(1, 4, 1):

                    for k in range(1, 3, 1):

                        if k == 1:
                                letterS = 'S'
                        elif k == 2:
                            letterS = 'P'

                        for j in range(1, 4, 1):
                               
                            substitution = str(i) + letterF + "_" + newFlex[1] + "_" + str(j) + letterS
                            reSubs = re.sub(pattern, substitution, line)
                            file.write(reSubs + "\n")

                

augmentLines(f, q3File.gr)
augmentLines(f, q3File.gi)