"""
Created on Tue Sep 17 11:41:47 2019
Finished on Wed Sep 17 12:00:00 2019

@author: Barrett

This document defines the pull_data function and creates a txt file containing
the cleaned up data from all dates of observation.

The data will be a 2d array containing time length of decay in the [:,0] (or 
top) row and the time of occurance in the [:,1] (or bottomw) row.

The function may be called by other documents.
This will certainly give the most updated information.

It is, perhaps, faster in the long run to run this file and update data.txt and
call the data from there.

The second method is what we do for the majority of the project.
"""

import numpy as np  # We use numpy for its excellent handling of data.
import glob         # We use glob for it excellent handling of files.

def pull_data(filename = None):
    """
    pull_data function
        inputs
            filename
		which file to read, defaults to None which will read them all

        outputs
            time_length_of_decay
                array 
                contains the time length of the decays (in ns) of the muons
                gets rid of values of muons that are not fully decayed or
                values when the detector detects nothing

            time_of_occurance
                array
                contains the time when the decay happened
                output is in seconds since Jan 1 00:00:00 1970
    """
    time_length_of_decay = []
    time_of_occurance = []
    
    if not filename:
        print("Number of files: " + str(len(glob.glob("Data/*.data"))))
        for filename in glob.glob("Data/*.data"):
            file = np.loadtxt(filename)
            print("Currently reading from", filename)
            print("This file is",len(file[:,0]),"lines long.")
            for i in range(len(file[:,0])):
                if file[i,0] < 20000:
                    time_length_of_decay.append(file[i,0])
                    time_of_occurance.append(file[i,1])
    else:
        print("Reading " + str(filename))
        file = np.loadtxt("Data/"+filename)
        for i in range(len(file[:,0])):
            if file[i,0] < 20000:
                time_length_of_decay.append(file[i,0])
                time_of_occurance.append(file[i,1])
            
    print("The Data has been reduced to ", len(time_length_of_decay), "lines.")
    return time_length_of_decay, time_of_occurance

if __name__ == '__main__':
    print("Rewriting data.txt")
    # The above command checks if this is being ran from here.
    time_length_of_decay, time_of_occurance = pull_data()
    # The above command calls the function.
    np.savetxt("data.txt",[time_length_of_decay,time_of_occurance])
    # The above command saves the output to a file called "data.txt".
        
