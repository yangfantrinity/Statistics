# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:46:53 2017

@author: yfan

to study exponential distribution
"""
import pandas as pd
import matplotlib.pyplot as plt
import Cdf
import myplot
import numpy as np
import math

def readData(): 
    BabyArrivalTime_array=[[1,    3837,      5],
        [1,    3334,      64],
        [2,    3554,      78],
        [2,    3838,     115],
        [2,    3625,     177],
        [1,    2208,     245],
        [1,    1745,     247],
        [2,    2846,     262],
        [2,    3166,     271],
        [2,    3520,     428],
        [2,    3380,     455],
        [2,    3294,     492],
        [1,    2576,     494],
        [1,    3208,     549],
        [2,    3521,    635],
        [1,    3746,    649],
        [1,    3523,     653],
        [2,    2902,     693],
        [2,    2635,     729],
        [2,    3920,     776],
        [2,    3690,     785],
        [1,    3430,     846],
        [1,    3480,     847],
        [1,    3116,     873],
        [1,    3428,     886],
        [2,    3783,     914],
        [2,    3345,     991],
        [2,    3034,    1017],
        [1,    2184,    1062],
        [2,    3300,    1087],
        [1,    2383,    1105],
        [2,    3428,    1134],
        [2,    4162,    1149],
        [2,    3630,    1187],
        [2,   3406,    1189],
        [2,   3402,    1191],
        [1,    3500,    1210],
        [2,    3736,   1237],
        [2,    3370,    1251],
        [2,    2121,    1264],
        [2,    3150,    1283],
        [1,    3866,    1337],
        [1,   3542,    1407],
        [1,    3278,    1435]
        ]

    BabyArrivalTime_df = pd.DataFrame(BabyArrivalTime_array)
    return BabyArrivalTime_df

def GetBirthInterval(data):
    
    data.columns = ['sex', 'birthweight', 'minutesfrommidnight']
    data['birthinterval']=data['minutesfrommidnight'].diff(1)
    return list(data['birthinterval'][1:])

def GetCcdf(cdf):
    ccdf_p = []
    ccdf_x = []
    for xs, ps in cdf.Items():
        ccdf_p.append(1-ps)
        ccdf_x.append(xs)
#    print (ccdf_x, ccdf_p)
    return ccdf_x, ccdf_p


def main():
    BabyBirthTime = readData()
    birthinterval = GetBirthInterval(BabyBirthTime)
    cdf_birthinterval = Cdf.MakeCdfFromList(birthinterval)
#    print cdf_birthinterval.Items()
    myplot.cdf(cdf_birthinterval)
    myplot.show()
#    myplot.Cdf(cdf_birthinterval, complement=True, xscale='linear', yscale='log')
#    myplot.show()
    ccdf_x, ccdf_p = GetCcdf(cdf_birthinterval)
    plt.plot(ccdf_x, ccdf_p)
    plt.yscale('log')
    plt.show()


if __name__=='__main__':
    main()

