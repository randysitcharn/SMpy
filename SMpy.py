#!/usr/bin/python3.6
#-*- coding: utf-8 -*-

from numpy import around
import datetime

class card:
    """Card primary_key:..., recto: recto of the card,verso: verso of the card"""
    def __init__(self,primary_key,recto,verso):
        self.primary_key=primary_key
        self.recto=recto
        self.verso=verso
    def __str__(self):
        return('primary_key: '+str(self.primary_key)+', recto: '+str(recto)+', verso: '+str(verso))

class icard:
    """information about a card's schedule, n: number of sights since the begining or restart,
        EF: E-factor,I: interval between last sigth and next sight, date: date of next sigth """
    def __init__(self, primary_key,n,EF,I,date):
        self.primary_key=primary_key
        self.n = n
        self.EF= EF
        self.date = date
        self.I= I
    def __str__(self):
        return('primary_key: '+str(self.primary_key)+', n: '+str(self.n)+', E-factor: '+str(self.EF)+', date: '+str(self.date)+', I:'+str(self.I))

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

def new_icard(icard, q):
    I=inter_repetition(i.n,i.EF,i.I)
    EF=e_factor(i.EF,q)
    if q < 3:
        res=icard(i.primary_key,0,EF,I,datetime.date.today()+datetime.timedelta(days=I))
    else:
        res=icard(i.primary_key,i.n+1,EF,I,datetime.date.today()+datetime.timedelta(days=I))

def SM2(icards, present):
    res=[]
    for i in icards:
        I=inter_repetition(i.n,i.EF,i.I)
        q=present(i)
        EF=e_factor(i.EF,q)
        if q < 3:
            icards.append(icard(i.primary_key,0,EF,I,datetime.date.today()+datetime.timedelta(days=I)))
        else:
            res.append(icard(i.primary_key,i.n+1,EF,I,datetime.date.today()+datetime.timedelta(days=I)))
    return(res)
