# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:58:53 2019

@author: Barrett
"""

import pandas as pd
import numpy as np
from pull_data import pull_data
import glob


data = pd.read_csv("data.txt",
            sep = " ",
            header = None)

data = data.transpose()
data.columns = ["decay_time","occurance_time"]

print("The decay time has a mean value of",np.mean(data["decay_time"]),"ns.")
print("It ranges from",np.min(data["decay_time"]),"ns to",
      np.max(data["decay_time"]),"ns.")

print("Number of files: " + str(len(glob.glob("Data/*.data"))))
#These print statements will help unerstand how many files you're reading.
# The following line goes through the files and reads them in.

list_of_events = []
list_of_decays = []
list_of_files  = []
for filename in glob.glob("Data/*.data"):
    file = pd.read_csv(filename,
                       sep = " ",
                       header = None,
                       dtype = np.float64)
    file.columns = ["clock_output","occurance_time"]
    decays = file[file["clock_output"] < 20000]
    events = file[file["clock_output"] < 40000]
    list_of_events.append(events)
    list_of_decays.append(decays)
    list_of_files.append(file)

print("This list is ",len(list_of_events),"long.")

total_time_seconds = []
total_time_hours = []
total_events = []
total_decays = []

for i in range(len(list_of_events)):
    trial = pd.DataFrame(list_of_events[i])
    trial.columns = ["event","occurance_time"]
    events = len(list_of_events[i])

    trial_decays = pd.DataFrame(list_of_decays[i])
    trial_decays.columns = ["decay","occurance_time"]
    decays = len(trial_decays["decay"])
   
    time = pd.DataFrame(list_of_files[i])
    time.columns = ["event","occurance_time"]
    time_seconds = np.max(time["occurance_time"]) - np.min(time["occurance_time"])
    time_hours = time_seconds/60/60

    total_time_seconds.append(time_seconds)
    total_time_hours.append(time_hours)
    total_events.append(events)
    total_decays.append(decays)

    print("---------------")
    print("Run",i,"lasted",time_hours,"hours.")
    print("Run",i,"had",events,"events.")
    print("This means there was an average of",events/time_seconds,"events per second")
    print("or",time_seconds/events,"seconds between events.")
    print("There were",decays,"decays for this run.")
    print("This means there were",decays/time_seconds,"decays per second")
    print("or",time_seconds/decays,"seconds between decays.")

print("------TOTAL------")
print("This means we had a total of",np.sum(total_events),"events")
print("with",np.sum(total_time_hours),"hours of observation.")
print("This corresponds to an average of",np.sum(total_events)/np.sum(total_time_seconds),"events per second")
print("or",np.sum(total_time_seconds)/np.sum(total_events),"seconds between events.")
print("We had a total of",np.sum(total_decays),"decays")
print("with",np.sum(total_decays)/np.sum(total_time_seconds),"decays per second")
print("or",np.sum(total_time_seconds)/np.sum(total_decays),"seconds between decays.")
