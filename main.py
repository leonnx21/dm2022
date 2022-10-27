import json
import re
import math

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
    if i>100000:
        break

def dfcount(textcollection):
    textdict = {}
    for i in textcollection:
        for word in i:
            if word not in textdict:
                textdict[word] = 1
        textdict[word] += 1
    dfdict = {}

    for key, value in textdict.items():
        df = int(value)/D
        idf = math.log(D/df)
        dfdict[key] = idf

    dfdict2 = sorted(dfdict.items(), key=lambda kv: kv[1])
    dfdict2.reverse()

    return dfdict2


fdict ={}
text = textcollection[10]

for word in text:
    if word not in fdict:
        fdict[word] = 1
fdict[word] += 1

tfdict = {}
for key, value in fdict.items():
    tf = value/len(text)
    tfdict[key] = tf

tf_dfdict ={}
for k1, v1 in dfdict.items():
    for k2, v2 in tfdict.items():
        if k1 == k2:
            tf_dfdict[k1] = v1*v2

tf_dfdict2 = sorted(tf_dfdict.items(), key=lambda kv: kv[1])
tf_dfdict2.reverse()

#print(textcollection)
#print(dfdict2)
print(tf_dfdict2)
