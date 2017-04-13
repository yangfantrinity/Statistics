# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:17:08 2017

@author: yfan
"""

import codesample
import numpy as np

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
    
    
def main():
    table = codesample.Pregnancies()
    table.ReadRecords()
    livebirth_record = livebirth(table.records)
    print 'number of live birth:', len(livebirth_record)
    first_baby, others = partitionRecord(livebirth_record.records)
#    print len(first_baby)
#    print len(others)
    print 'average pregnancy length of first baby in weeks:', avgprglength(first_baby.records)
    print 'average pregnancy length of non first baby in weeks:', avgprglength(others.records)
    

if __name__ ==  '__main__':
    main()
