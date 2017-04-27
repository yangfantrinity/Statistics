# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:42:40 2017

@author: yfan

to do Exercise 5.6, but not completed yet
"""
import random
import numpy as np
import thinkstats
import erf
import myplot
import Cdf
from scipy.special import erf, erfinv

root2 = np.sqrt(2)

def GetNormalList(NumberOfItems, mu, sigma):
    NormalList = []
    for i in range(0, NumberOfItems):
        NormalList.append(random.normalvariate(mu, sigma))
    return sorted(NormalList)


def GetListOfList(NumberOfItems, mu, sigma, LenOfList):
    ListOfSamples = []
    for i in range(LenOfList):
        samples = GetNormalList(NumberOfItems, mu, sigma)
        ListOfSamples.append(samples)
    return zip(*ListOfSamples)

def GetMean(x):
    return float(np.sum(x))/len(x)
    

def GetSD(x):
    var = thinkstats.Var(x)
    SD = np.sqrt(var)
#    print SD
    return SD

spread = 4.0

def GetNormalCdf(mu, sigma, low=-spread, high=spread, digits=2):
    n = (high - low) * 10**digits + 1
    xs = np.linspace(low*sigma+mu, high*sigma+mu, n)
    ps = (erf(((xs - mu) / sigma) / root2) + 1) / 2
    cdf = Cdf.Cdf(xs, ps)
    return cdf


def main():
    result = GetListOfList(4, 950, 50, 1000)
#    print result
    mean = [GetMean(x) for x in result]
    print len(result)
    print mean
    print mean[len(mean)-1]
    NewMean =  mean[len(mean)-1]
    
    
    NewList = list(result[len(result)-1])
#    print NewList
    SampleCdf = Cdf.MakeCdfFromList(NewList, 'SampleCdf')
#    myplot.Cdf(SampleCdf)
#    myplot.show()
    
    
    SD = GetSD(np.array(NewList))
    print SD
    NewCdf = GetNormalCdf(NewMean, SD)
    NewCdf.name = 'StandardNormal'
#    test = erf.MakeNormalCdf()
#    print test.Values()
#    
    myplot.Cdfs([NewCdf, SampleCdf])
    myplot.show()
    
    
  
    


if __name__=='__main__':
    main()
        

        