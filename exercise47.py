# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:14:00 2017

@author: yfan
"""

import erf

mu = 100
sigma = 15
total_population = 6000000000
fraction_greatermean = erf.NormalCdf(mu, mu, sigma)

test = [115, 130, 145]
print 'greater than 115:', 1-erf.NormalCdf(test[0], mu, sigma)
print 'greater than 130:', 1-erf.NormalCdf(test[1], mu, sigma)
print 'greater than 145:', 1-erf.NormalCdf(test[2], mu, sigma)
print 'six-sigma:', (1-erf.NormalCdf(6*sigma+mu, mu, sigma))*total_population