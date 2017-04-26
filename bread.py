# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:42:40 2017

@author: yfan
"""
import random

def GetNormalList(NumberOfItems, mu, sigma):
    NormalList = []
    for i in range(NumberOfItems):
        NormalList.append(random.normalvariate(mu, sigma))