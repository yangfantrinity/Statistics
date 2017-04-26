# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:44:01 2017

@author: yfan

solution to Pareto Distribution and Weibull Distribution in Think Stats
"""

import random
import Cdf
import myplot
import matplotlib.pyplot as plt
import numpy as np

def paretovariate(xm, alpha):
#    print xm*random.paretovariate(alpha)
    return xm*random.paretovariate(alpha) 

def GetWeibullList(NumberOfItems, alpha, beta):
    WeibullList = []
    for i in range(NumberOfItems):
        WeibullList.append(random.weibullvariate(alpha, beta))
    return WeibullList


def GetParetoList(NumberOfItems,xm, alpha):
    ParetoList = []
    for i in range(NumberOfItems):
        ParetoList.append(paretovariate(xm,alpha))
    return ParetoList

def GetCcdf(x):
    """
    to compute compensate CDF
    """
    cdf = Cdf.MakeCdfFromList(x)
    ccdf = Cdf.Cdf()
    for xs, ps in cdf.Items():
        ccdf.Append(xs, 1-ps)
#    print ccdf.Items()    
    return ccdf

def GetLogCcdf(x):
    """
    to transform the probability value to its log value
    """
    ccdf = GetCcdf(x)
    LogCcdf = Cdf.Cdf()
    for xs, ps in ccdf.Items():
        LogCcdf.Append(xs, -np.log(ps))
        
#    print LogCcdf.Items()    
    return LogCcdf

def GetMin(x):
    return np.min(x)
        

def PlotLogYCcdf(x):
    """
    to plot the compensate CDF in a log-log scale
    """
    ccdf = GetCcdf(x)
    xs, ps = ccdf.Render()
    plt.plot(xs, ps)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
def PlotLogLogYCcdf(x):
    """
    to transform weibull distribution CDF to plot it as a straight line
    and plot in a log(log)-log scale
    """
    LogCcdf = GetLogCcdf(x)
    xs, ps = LogCcdf.Render()
    plt.plot(xs, ps)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    


def main():
    ParetoList = GetParetoList(6000000, 100, 1.7)
   
    PlotLogYCcdf(ParetoList)
    
    cdf = Cdf.MakeCdfFromList(ParetoList)
    print 'Median value:', cdf.Percentile(50)
    print 'Mean value:', cdf.Mean()
    print 'Percentage of people shorter than the mean height:', cdf.Prob(cdf.Mean())
    print 'minimum:', GetMin(ParetoList)
    
    myplot.Cdf(cdf)
    myplot.show()
    WeibullList = GetWeibullList(1000, 1, 1.5)
    cdf = Cdf.MakeCdfFromList(WeibullList)
    myplot.Cdf(cdf)
    myplot.show() 
    PlotLogLogYCcdf(WeibullList)
    
    
    
  
    
if __name__ == '__main__':
    main()
    
    
 
    
