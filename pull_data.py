"""
Created on Tue Sep 17 11:41:47 2019
Finished on Tue Sep 17  2019

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

def pull_data():
    """
    pull_data function
        inputs
            none

        outputs
            time_length_of_decay
                array 
                contains the time length of the decays (in ns) of the muons

            time_of_occurance
                array
                contains the time when the decay happened
                output is in seconds since Jan 1 00:00:00 1970
    """
    time_length_of_decay = []
    time_of_occurance = []
    
    for filename in glob.glob("Data/*.data"):    
        file = np.loadtxt(filename)
        for i in range(len(file[:,0])):
            if file[i,0] < 20000:
                time_length_of_decay.append(file[i,0])
                time_of_occurance.append(file[i,1])
    
    return time_length_of_decay, time_of_occurance

time_length_of_decay, time_of_occurance = pull_data()
np.savetxt("data.txt",[time_length_of_decay,time_of_occurance])