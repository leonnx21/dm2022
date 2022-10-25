import json
import re
import math
from collections import Counter

data_file = open("/media/leon/MCU/USTH/Data mining/DataMining data/yelp_academic_dataset_review.json")
D = 0
textcollection = []

for i, line in enumerate(data_file):
    x = json.loads(line)['text']
    x2 = x.lower()
    x3 = re.sub(r'[^\w\s]', '', x2)
    x4 = x3.split()
    textcollection.append(x4)
    D += 1
    if i>2000:
        break

textdict = {}

for i in textcollection:
    for word in i:
        if word not in textdict:
            textdict[word] = 1
    textdict[word] += 1

dfdict = {}

for key, value in textdict.items():
    df = int(value)/D
    idf = math.log(1/df)
    dfdict[key] = idf

dfdict2 = sorted(dfdict.items(), key=lambda kv: kv[1])
dfdict2.reverse()

print(dfdict2)
