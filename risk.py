# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:12:06 2017

@author: Sunny
"""
import codesample
import Pmf
import first
#
def getListFromObj(records):
    attr = [record.prglength for record in records]
    return attr


def ProbEarly(pmf):
    """
    calculated the probability that a baby was born during Week 37 or earlier
    """
    prob = 0
    for week in range(1,38):
        prob += float(pmf.Prob(week))
    return prob

    
    
#def ProbOnTime(pmf):
#    
#    
#    
#    
#    
#def ProbLate(pmf):
#    
#    
#    
    
    
def main():
    table = codesample.Pregnancies()
    table.ReadRecords()
    livebirth_record = first.livebirth(table.records)
    first_baby, others = first.partitionRecord(livebirth_record.records)
    
    prglength_livebirth = getListFromObj(livebirth_record.records)
    pmf_livebirth = Pmf.MakePmfFromList(prglength_livebirth)
    
#    pmf_firstbaby = Pmf.MakePmfFromList(first_baby.records)
#    pmf_others = Pmf.MakePmfFromList(others.records)
#    print pmf_livebirth.Render()
#    print pmf_livebirth.Prob(13)
    
    print 'probability of early born of all live birth babies:', ProbEarly(pmf_livebirth)
    
    
    
    
    
    
if __name__ == '__main__':
    main()