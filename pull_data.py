# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:41:47 2019

@author: Barrett
"""

import numpy as np
import glob

    

def pull_data(x = "10293841098"):
    if x != "10293841098":
        print("Matt, what are you wearing?")

    data = []
    
    for filename in glob.glob("Data/*.data"):    
        file = np.loadtxt(filename)
        for i in range(len(file[:,0])):
            if file[i,0] < 20000:
                data.append(file[i,:])
    
    return data

data = pull_data()
np.savetxt("data.txt",data)