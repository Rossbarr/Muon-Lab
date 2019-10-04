"""
Created on Tue Sep 17 11:41:47 2019

@author: Barrett and Matt

This document defines the pull_data function and creates a txt file containing
the cleaned up data from all dates of observation.

The data will be a 2d array containing time length of decay in the [:,0] (or 
top) row and the time of occurance in the [:,1] (or bottomw) row.

The function may be called by other documents.
This will certainly give the most updated information.

It's faster to run this file to update data.txt and call the data from there.

The second method is what we do for the majority of the project.
"""

import numpy as np  # We use numpy for its excellent handling of data.
import glob         # We use glob for it excellent handling of files.

def pull_data(filename = None):
    """
    pull_data function
        inputs
            filename
                string
                file to read, defaults to None which will read them all

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
    time_length_of_decay = []   # Setting up arrays
    time_of_occurance = []      # Setting up arrays
    
    if not filename:
        print("Number of files: " + str(len(glob.glob("Data/*.data"))))
        # These print statements will help unerstand how many files you're
        # reading.
        for filename in glob.glob("Data/*.data"):   # Goes through the files.
            file = np.loadtxt(filename)             # Reads the files in. 
            print(filename, len(file[:,0]))         # Print Statement.
            for i in range(len(file[:,0])):                 # Finds the "good"
                if file[i,0] < 20000:                       # data points and
                    time_length_of_decay.append(file[i,0])  # Reads them into
                    time_of_occurance.append(file[i,1])     # the arrays.
    
    else:
        print("Reading " + str(filename))       # Print Statement.
        file = np.loadtxt("Data/"+filename)     # Reads the file in.
        for i in range(len(file[:,0])):                 # Finds the "good" data
            if file[i,0] < 20000:                       # points and reads them
                time_length_of_decay.append(file[i,0])  # into the arrays.
                time_of_occurance.append(file[i,1])
            
    print("The Data has ", len(time_length_of_decay), "lines.")
    # This print statement will help understand the number of points you have.
    return time_length_of_decay, time_of_occurance

if __name__ == '__main__':
    # The above command checks if this is being ran from here.
    print("Rewriting data.txt")
    time_length_of_decay, time_of_occurance = pull_data()
    # The above command calls the function.
    np.savetxt("data.txt",[time_length_of_decay,time_of_occurance])
    # The above command saves the output to a file called "data.txt".
        
