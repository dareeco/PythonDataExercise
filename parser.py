import re



def parser():
    f = open("example.txt", "r")
    data = f.read()
    xcount = len(re.findall(r'\.', data))
    ycount = len(re.findall(r'\!', data))
    brojRechenici = xcount + ycount
    brojB = len(data)
    Rechnik={}
    stats={}
    stats["total_sentences"]=brojRechenici
    stats["total_characters"]=brojB


    sentences=[sen for sen in re.split('\.|!|\?', data) if len(sen) > 2]
    Rechnik["sentencs"]=sentences
    Rechnik["stats"]=stats
    #The sentences are split into a list



    return Rechnik