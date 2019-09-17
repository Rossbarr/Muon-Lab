# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:35:25 2019

@author: Barrett
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


Data1 = np.loadtxt("Data/9-10-19_12-6.data")

Time = Data1[:,1]
Detection = Data1[:,0]

Muon = []
for i in Detection:
    if i < 20000:
        Muon.append(i)
        

print(Muon)

plt.hist(Muon)
plt.figure(figsize = [10,10])
plt.show()