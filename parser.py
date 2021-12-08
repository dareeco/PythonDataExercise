import nltk.tokenize

import re
from nltk import tokenize


def Parser():
    f = open("example.txt", "r")
    data = f.read()
    xcount = len(re.findall(r'\.', data))
    ycount = len(re.findall(r'\!', data))
    brojRechenici = xcount + ycount
    brojB = len(data)
    stats={}
    stats["total_sentences"]=brojRechenici
    stats["total_characters"]=brojB


    sentences=[sen for sen in re.split('\.|!|\?', data) if len(sen) > 2]
    #The sentences are split into a list



    return sentences,stats