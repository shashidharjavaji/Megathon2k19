# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:49:22 2019

@author: DELL
"""


def hNvalidation(sentence):
    flag = 1

    Length = len(sentence)
    if (Length > 4):
        for i in range(Length):
            if (i+4 < Length):
                if (sentence[i]==' ' and sentence[i+1]=='h' and sentence[i+2]==' ' and sentence[i+3]=='N' and sentence[i+4]==' '):
                    flag = 0


    return flag
