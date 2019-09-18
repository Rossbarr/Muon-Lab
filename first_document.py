# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:35:25 2019

@author: Barrett
"""

import numpy as np
import scipy as sp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt')

decay = data[0,:]
time = data[1,:]

time0 = []
for i in range(len(time)-1):
    time0.append(time[i+1] - time[1])

plt.hist(time0,bins=1000)

