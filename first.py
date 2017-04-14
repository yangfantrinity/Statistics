# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:17:08 2017

@author: yfan
"""

import codesample
import numpy as np
from thinkstats import Mean, MeanVar, Var
import Pmf
from operator import itemgetter
import matplotlib.pyplot as pyplot
#import pandas as pd


#print 'Number of pregnancies records:', len(table.records)
def livebirth(records):
    livebirth_record = codesample.Pregnancies()
    for i, record in enumerate(records):
        if record.outcome == 1:
            livebirth_record.AddRecord(record)
    return livebirth_record
  
#
def partitionRecord(records):
    first_baby = codesample.Pregnancies()
    others = codesample.Pregnancies()
    
    for i, record in enumerate(records):
        if (record.birthord == 1):
            first_baby.AddRecord(record)
        else:
            others.AddRecord(record)
    return first_baby, others
    
def avgprglength(records):
    
    total_length = float(np.sum(record.prglength for record in records))
    avg_length = total_length/len(records)
    return avg_length

def standardDev(records):
    attr = [record.prglength for record in records]
    var = Var(np.array(attr))
    return np.sqrt(var)

def attrMean(records):
    attr = [record.prglength for record in records]
    mean = Mean(np.array(attr))
    return mean

def AllModes(records):
    """
    print the value-frequency pair in ascending order
    """
    attr = [record.prglength for record in records]
    hist = Pmf.MakeHistFromList(attr)
    getfreq = itemgetter(1)
    print sorted(hist.Items(), key = getfreq)
    return hist

def plot_bar(hist):
    vals, freqs = hist.Render()
    rectangles = pyplot.bar(vals, freqs)
    pyplot.show()    
    
def main():
    table = codesample.Pregnancies()
    table.ReadRecords()
    livebirth_record = livebirth(table.records)
    print 'number of live birth:', len(livebirth_record)
    first_baby, others = partitionRecord(livebirth_record.records)
#    print len(first_baby)
#    print len(others)
    avg_firstbaby = avgprglength(first_baby.records)
    avg_others = avgprglength(others.records)
    print 'average pregnancy length of first baby in weeks:', avg_firstbaby
    print 'average pregnancy length of non first baby in weeks:', avg_others
    print (avg_firstbaby - avg_others)*7.0
    
    dev_firstbaby = standardDev(first_baby.records)
    dev_others = standardDev(others.records)
    print 'standard deviation of first baby in weeks:', dev_firstbaby
    print 'standard deviation of non first baby in weeks:', dev_others
    print (dev_firstbaby - dev_others)*7.0
          
    hist_firstbaby = AllModes(first_baby.records)
    plot_bar(hist_firstbaby)
    
    

if __name__ ==  '__main__':
    main()
