# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:15:08 2017

@author: yfan
"""

"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import random 

def PercentileRank(scores, your_score):
    """Computes the percentile rank relative to a sample of scores."""
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank

scores = [55, 66, 77, 88, 99]
your_score = 88

print 'score, percentile rank'
for score in scores:
    print score, PercentileRank(scores, score)
print

def Percentile(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank. """
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score

def Percentile2(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank.

    Slightly more efficient.
    """
    scores.sort()
    index = percentile_rank * (len(scores)-1) / 100
    return scores[index]

## this function has some problem when called in first.py
def Percentile_select(data, percentile_rank):
    "Find the nth rank ordered element (the least value has rank 0)."
    n = percentile_rank * (len(scores)-1) / 100
    data = list(data)
    if not 0 <= n < len(data):
        raise ValueError('not enough elements for the given rank')
    while True:
        pivot = random.choice(data)
        pcount = 0
        under, over = [], []
        uappend, oappend = under.append, over.append
        for elem in data:
            if elem < pivot:
                uappend(elem)
            elif elem > pivot:
                oappend(elem)
            else:
                pcount += 1
        if n < len(under):
            data = under
        elif n < len(under) + pcount:
            return pivot
        else:
            data = over
            n -= len(under) + pcount
                    
print 'prank, score, score, score'
for percentile_rank in [0, 20, 25, 40, 50, 60, 75, 80, 100]:
    print percentile_rank, 
    print Percentile(scores, percentile_rank),
    print Percentile2(scores, percentile_rank),
    print Percentile_select(scores, percentile_rank)