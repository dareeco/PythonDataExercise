import sys
import os
import re

def counter(data):
    xcount = len(re.findall(r'\.', data))
    ycount = len(re.findall(r'\!', data))
    total_sentences = xcount + ycount
    data.replace(" ", "")
    brojB = len(data)
    return total_sentences,brojB