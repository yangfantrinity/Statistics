# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:12:08 2017

@author: yfan
"""
import codesample
import Pmf
import first
import risk
import numpy as np
import matplotlib.pyplot as pyplot

def remove_x(pmf,x):
    all_values = pmf.Values()
    for value in all_values:
        if value <x:
#            print value
            pmf.Remove(value)
#    print pmf.Items()
#    print np.sum(pmf.Probs())
    return pmf

def conditionalProb(pmf):
    pmf.Normalize()
#    print np.sum(pmf.Probs())
    return pmf

def all_conditionalProb():
    """
    computes the conditional probability that a baby will be born in week x for x in all week
    """
    table = codesample.Pregnancies()
    table.ReadRecords()
    livebirth_record = first.livebirth(table.records)
    first_baby, others = first.partitionRecord(livebirth_record.records)
    probs_firstbaby = [] 
    probs_others = []
    for x in range(35, 46):
#        prglength_livebirth = risk.getListFromObj(livebirth_record.records)
#        pmf_livebirth = Pmf.MakePmfFromList(prglength_livebirth)
#        pmf_livebirth_x = remove_x(pmf_livebirth, x)
#        pmf_livebirth_cp = conditionalProb(pmf_livebirth_x)
#        print 'all live birth:', (x, pmf_livebirth_cp.Prob(x))
        
        prglength_firstbaby = risk.getListFromObj(first_baby.records)
        pmf_firstbaby = Pmf.MakePmfFromList(prglength_firstbaby)
        pmf_firstbaby_x = remove_x(pmf_firstbaby, x)
        pmf_firstbaby_cp = conditionalProb(pmf_firstbaby_x)
#        print 'first baby:', (x, pmf_firstbaby_cp.Prob(x))
        probs_firstbaby.append(pmf_firstbaby_cp.Prob(x))
        
        prglength_others = risk.getListFromObj(others.records)
        pmf_others = Pmf.MakePmfFromList(prglength_others)
        pmf_others_x = remove_x(pmf_others,x)
        pmf_others_cp = conditionalProb(pmf_others_x)
#        print 'non first baby:', (x, pmf_others_cp.Prob(x))
        probs_others.append(pmf_others_cp.Prob(x))
        
    return probs_firstbaby, probs_others    

def plot_prob(probs1, probs2):
    pyplot.plot(probs1, 'r')
    pyplot.plot(probs2, 'b')
    pyplot.show()
    

def main(): 
    probs_firstbaby, probs_others = all_conditionalProb()
    print probs_firstbaby
    print probs_others
    plot_prob(probs_firstbaby, probs_others)
    
if __name__ == '__main__':
    main()