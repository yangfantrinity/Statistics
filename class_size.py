# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:35:02 2017

@author: yfan
"""
import Pmf
import myplot

#class class_size(size, count):
#    def __init__(self):
#        self.size = size
#        self.count = count
        

def sampleRecords():
    class_size = { 7: 8, 
                  12: 8, 
                  17: 14, 
                  22: 4, 
                  27: 6, 
                  32: 12, 
                  37: 8, 
                  42: 3, 
                  47: 2, 
                  }
    
    return class_size
    
def getPmf(record_dict):
    pmf_classsize = Pmf.MakePmfFromDict(record_dict)
    print pmf_classsize.Items()
    pmf_classsize.name = 'observed'
    return pmf_classsize

def UnbiasPmf(pmf, name):
    """
    uses the .Mult to scale the frequency/probability with the value x
    """
    new_pmf = pmf.Copy()
    new_pmf.name = name
    for x in new_pmf.Values():
        new_pmf.Mult(x, 1.0/x)
        
    new_pmf.Normalize()
    print new_pmf.Items()
    return new_pmf



def main():
    class_size = sampleRecords()
    pmf_classsize = getPmf(class_size)
    unbiased_pmf = UnbiasPmf(pmf_classsize, 'unbiased')
    myplot.Pmfs([pmf_classsize, unbiased_pmf])
    myplot.show()
    
if __name__ == '__main__':
    main()