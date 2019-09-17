# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:35:25 2019

@author: Barrett
"""

import numpy as np
import scipy as sp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from pull_data import pull_data

data = pull_data()

counts, bins, patches = plt.hist(Muon)

def exponential_decay(x, a, b, c):
    return a*np.exp(b*x) - c

def custom_fit(t,A_neg,tau_0,tau_c,A_pos,C):
	return A_neg*np.exp(-t*(1/tau_0+1/tau_c))+A_pos*np.exp(-t/tau_0)

x = []
for i in range(len(bins)-1):
    x.append((bins[i] + bins[i+1])/2)

popt, pcov = curve_fit(exponential_decay, counts, x, p0 = [160,1e-6, 1])

y = []
for i in range(len(x)):
    y.append(exponential_decay(x[i], popt[0], popt[1], popt[2]))

plt.hist(Muon, label = "Data")
plt.plot(y, x, label = "Fit")
plt.legend()
plt.figure(figsize = [8,10])
plt.show()