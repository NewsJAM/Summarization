# -*- coding: utf-8 -*-
import mecab
import Fuzzy

def score(subject,s):
    # the count of common nouns
    subNN = mecab.NN(subject.encode('utf-8'))
    i = 0
    for subnoun in subNN:
        if len(s.encode('utf-8').split(subnoun))>1:
            i = i+1

    temp = mecab.NN(s.encode('utf-8'))
    j = len(temp)
    z = 1
    if j==0:
        j = 1
        z = 0

    temp = mecab.JX(s.encode('utf-8'))
    k = 0
    if len(temp)>0:
        k = len(temp)

    temp = mecab.JKB(s.encode('utf-8'))
    l = 0
    if len(temp)>0:
        l = len(temp)

    input1 = 1.5*z*i/j
    input2 = 2.*(k+l)/j
    if input1 > 1.:
        input1 = 1.
    if input2 > 1.:
        input2 = 1.
    return float(Fuzzy.inf( input1, input2 ))


