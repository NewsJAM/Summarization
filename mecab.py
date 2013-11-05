# -*- coding: utf-8 -*-

import MeCab
import sys
import string
def NN(sentence):
    try:
        t = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ko-dic/')
        m = t.parseToNode(sentence)
        parsed = []
        while m:
            if m.feature.split(',')[0]=='NN':
                parsed.append(m.surface)
            m = m.next
        return parsed

    except RuntimeError, e:
        print "RuntimeError:", e;

def JX(sentence):
    try:
        t = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ko-dic/')
        m = t.parseToNode(sentence)
        parsed = []
        while m:
            if m.feature.split(',')[0]=='JX':
                parsed.append(m.surface)
            m = m.next
        return parsed

    except RuntimeError, e:
        print "RuntimeError:", e;


def JKB(sentence):
    try:
        t = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ko-dic/')
        m = t.parseToNode(sentence)
        parsed = []
        while m:
            if m.feature.split(',')[0]=='JKB':
                parsed.append(m.surface)
            m = m.next
        return parsed

    except RuntimeError, e:
        print "RuntimeError:", e;

