# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:12:06 2017

@author: Sunny
"""
import codesample
import Pmf
import first
import numpy as np
#
def getListFromObj(records):
    attr = [record.prglength for record in records]
    return attr


def ProbEarly(pmf):
    """
    calculates the probability that a baby was born during Week 37 or earlier
    """
    prob = 0
    for week in range(1,38):
        prob += float(pmf.Prob(week))
    return prob

    
    
def ProbOnTime(pmf):
    """
    calculates the probability that a baby was born during 38, 39 or 40 weeks
    """
    prob = 0
    for week in range(38, 41):
        prob += float(pmf.Prob(week))
    return prob
    
    
    
def ProbLate(pmf):
    """
    calculates the probability that a baby was born later thqan 41 weeks
    """
    prob = 0
    max_value = np.max(pmf.Values())
#    print max_value
    for week in range(41,max_value+1):
        prob += pmf.Prob(week)
    return prob
    
    
    
    
def main():
    """
    computes the risk of a first baby being born early compare to non-first baby
    """
    table = codesample.Pregnancies()
    table.ReadRecords()
    livebirth_record = first.livebirth(table.records)
    first_baby, others = first.partitionRecord(livebirth_record.records)
    
    prglength_livebirth = getListFromObj(livebirth_record.records)
    pmf_livebirth = Pmf.MakePmfFromList(prglength_livebirth)
    prglength_firstbaby = getListFromObj(first_baby.records)
    pmf_firstbaby = Pmf.MakePmfFromList(prglength_firstbaby)
    prglength_others = getListFromObj(others.records)
    pmf_others = Pmf.MakePmfFromList(prglength_others)
#    print pmf_livebirth.Render()
#    print pmf_livebirth.Prob(13)
    
    print 'probability of early born, on time, and late born of all live birth babies:'
    print ProbEarly(pmf_livebirth)
    print ProbOnTime(pmf_livebirth)
    print ProbLate(pmf_livebirth)
    print 'probability of early born, on time, and late born of all first babies:'
    print ProbEarly(pmf_firstbaby) 
    print ProbOnTime(pmf_firstbaby)
    print ProbLate(pmf_firstbaby)
    print 'probability of early born, on time, and late born of all not first babies:'
    print ProbEarly(pmf_others) 
    print ProbOnTime(pmf_others)
    print ProbLate(pmf_others)
    
    
    
    
    
    
if __name__ == '__main__':
    main()