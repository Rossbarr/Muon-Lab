# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:35:25 2019

@author: Barrett
"""

import numpy as np
import scipy as sp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


Data1 = np.loadtxt("Data/9-10-19_12-6.data")

Time = Data1[:,1]
Detection = Data1[:,0]

Muon = []
for i in Detection:
    if i < 20000:
        Muon.append(i)

n, bins, patches = plt.hist(Muon)

def exponential_decay(x, a, b, c):
    return a*np.exp(b*x) - c

m = []
for i in range(len(bins)-1):
    m.append((bins[i] + bins[i+1])/2)

params, pcov = curve_fit(exponential_decay, n, m, p0 = [1,1e-6,1])

y = exponential_decay(n, params[0], params[1], params[2])

plt.hist(Muon, label = "Data")
plt.plot(n, y, label = "Fit")
plt.legend()
plt.figure(figsize = [8,10])
plt.show()