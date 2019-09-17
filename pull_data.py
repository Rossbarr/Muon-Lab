# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:41:47 2019

@author: Barrett
"""

import numpy as np
import glob

def pull_data():
    datas = []
    for filename in glob.glob("Data/*.data"):
        for i in range(len(filename)
            datas.append(np.loadtxt(filename))
    
    
    return data