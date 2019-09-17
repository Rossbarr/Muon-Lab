"""
Created on Tue Sep 17 11:41:47 2019
Finished on Tue Sep 17 17:29:11 2019

@author: Barrett

This document solely defines the pull_data function.
This function will be called upon by other documents to pull the data.
The data will be a 2d array containing time length of decay in the [:,0] (or 
left) column and the time of occurance in the [:,1] (or right) column.

Running this document will create (or replace) a txt file called data.txt.
This file contains the 2darray the function spits out, so one may examine it.
"""

import numpy as np  # we use numpy for its excellent handling of data
import glob         # we use glob for it excellent handling of files

def pull_data(x = "10293841098"):
    """
    pull_data function
        inputs
            x
                optional; if not 10293841098, then prints funny statement

        outputs
            data
                numpy.ndarray; 2d array containing time length of decay and
                time of occurance
                
    """
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