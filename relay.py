# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:24:01 2017

@author: yfan
"""

"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import urllib

import myplot
import Pmf
import Cdf
import score_example

results = 'http://www.coolrunning.com/results/10/ma/Apr25_27thAn_set1.shtml'

"""
Sample line.

Place Div/Tot  Div   Guntime Nettime  Pace  Name                   Ag S Race# City/state              
===== ======== ===== ======= =======  ===== ====================== == = ===== ======================= 
    1   1/362  M2039   30:43   30:42   4:57 Brian Harvey           22 M  1422 Allston MA              
"""

def ConvertPaceToSpeed(pace):
    """Converts pace in MM:SS per mile to MPH."""
    m, s = [int(x) for x in pace.split(':')]
    secs = m*60 + s
    mph  = 1.0 / secs * 60 * 60 
    return mph


def CleanLine(line):
    """Converts a line from coolrunning results to a tuple of values."""
    t = line.split()
    if len(t) < 6:
        return None
    
    place, divtot, div, gun, net, pace = t[0:6]

    if not '/' in divtot:
        return None

    for time in [gun, net, pace]:
        if ':' not in time:
            return None

    return place, divtot, div, gun, net, pace


def ReadResults(url=results):
    """Read results from coolrunning and return a list of tuples."""
    results = []
    conn = urllib.urlopen(url)
    for line in conn.fp:
        t = CleanLine(line)
        if t:
            results.append(t)
    return results


def GetSpeeds(results, column=5):
    """Extract the pace column and return a list of speeds in MPH."""
    speeds = []
    for t in results:
        pace = t[column]
        speed = ConvertPaceToSpeed(pace)
        speeds.append(speed)
    return speeds

def GetDivSpeeds(results, divname, speedcol = 5, column = 2 ):
    """
    extracts the speeds with division column = divname and return a list of speeds in MPH.
    """
    speeds = []
    for t in results:
        div = t[column]
        if div == divname:
            pace = t[speedcol]
            speed = ConvertPaceToSpeed(pace)
            speeds.append(speed)
    return speeds

def BiasPmf(pmf, speed):
    observed_pmf = pmf.Copy()
    for value in pmf.Values():
        speed_diff = abs(value - speed)
        observed_pmf.Mult(value, speed_diff)
#    print observed_speed
    return observed_pmf
    

def main():
    results = ReadResults()
    speeds = GetSpeeds(results)
#    pmf = Pmf.MakePmfFromList(speeds, 'speeds')
#    myplot.Pmf(pmf)
#    myplot.Show(title='PMF of running speed',
#               xlabel='speed (mph)',
#               ylabel='probability')
#    observed_pmf = BiasPmf(pmf, 7.5)
#    myplot.Pmf(observed_pmf)
#    myplot.Show(title='Biased PMF of running speed at 7.5',
#               xlabel='speed (mph)',
#               ylabel='probability')
    cdf = Cdf.MakeCdfFromList(speeds, 'speeds')
    myplot.Cdf(cdf)
    myplot.Show(title='CDF of running speed',
               xlabel='speed (mph)',
               ylabel='cumulative probability')
    print len(speeds)
    percentile_author = score_example.PercentileRank(speeds, speeds[96])
    print 'percentile of the author:', percentile_author
    
    div_speed = GetDivSpeeds(results,'M4049')
    print len(div_speed)
    percentile_div = score_example.PercentileRank(div_speed, speeds[96])
    print 'percentile of the author in his own division:', percentile_div
    
    div_speed2 = GetDivSpeeds(results, 'M5059')
    expected_speed = score_example.Percentile_select(div_speed2, percentile_div)
    print 'the author needs to run slower by:', expected_speed - speeds[96]

    


if __name__ == '__main__':
    main()