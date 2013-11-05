# -*- coding:utf-8 -*-
import re

def splitS(paragraph):
    ''' split a praragraph into sentences '''
    sentenceRule = re.compile(u"(\S.+?[.])(?=\s+|$)")
    sentenceList = sentenceRule.split(paragraph)

    temp = []
    for sentence in sentenceList:
        # REMOVE the special character
        sentence = sentence.replace(u'\u25B2',u'') #REMOVE: BLACK RIGHT-POINTING TRIANGLE
        sentence = sentence.replace(u'\u25B6',u'') #REMOVE: Black Square
        sentence = sentence.replace(u'\u25A0',u'')

        # REMOVE the return or tab
        sentence = sentence.replace(u'\n',u'')
        sentence = sentence.replace(u'\t',u'')
        sentence = sentence.replace(u'\r',u'')

        # REMOVE the content in the bracket
        pattern1 = re.compile(u"<([^>]+)>")
        sentence = re.sub(pattern1,'',sentence)

        # SPLIT the case of korean.korean
        pattern2 = re.compile(ur"(\S.+?[가-힣][.][가-힣]*?)")
        sentence = pattern2.split(sentence)

        # Print sentence
        if (type(sentence)==list):
            for u in sentence:
                if (u!='') and (u!=' ') and (u!='.'):
                    temp.append(u)
        else:
            temp.append(sentence)

    return temp 
