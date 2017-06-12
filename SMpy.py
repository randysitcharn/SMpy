#!/usr/bin/python3.6
#-*- coding: utf-8 -*-

from numpy import around

def e_factor(EF=None,q=None):
    if EF==None and q==None:
        EF=2.5
    else:
        EF = EF+(0.1-(5-q)*(0.08+(5-q)*0.02))
        if EF < 1.3:
            EF = 1.3
    return(EF)

def inter_repetition(n=None,EF=None,I=None):
    if n==0:
        return(0.0)
    elif n==1:
        return(1.0)
    elif n==2:
        return(6.0)
    else:
        return(around(I*EF))

def SM2(cards):
