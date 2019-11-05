# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:58:53 2019

@author: Barrett
"""

import pandas as pd
import numpy as np
from pull_data import pull_data

data = pd.read_csv("data.txt",
            sep = " ",
            header = None)

data = data.transpose()
data.columns = ["decay_time","occurance_time"]

print("The decay time has a mean value of",np.mean(data["decay_time"]),"ns.")
print("It ranges from",np.min(data["decay_time"]),"ns to",
      np.max(data["decay_time"]),"ns.")

data1 = pd.read_csv("Data/9-24-19_12-6.data",
            sep = " ",
            header = None)
events1 = pull_data("9-24-19_12-6.data")

data1.columns = ["decay_time","occurance_time"]

data2 = pd.read_csv("Data/9-10-19_12-6.data",
            sep = " ",
            header = None)
events2 = pull_data("9-10-19_12-6.data")

data2.columns = ["decay_time","occurance_time"]

data3 = pd.read_csv("Data/10-1-19_11-7.data",
            sep = " ",
            header = None)
events3 = pull_data("10-1-19_11-7.data")

data3.columns = ["decay_time","occurance_time"]

data4 = pd.read_csv("Data/9-10-19_9-12-19.data",
            sep = " ",
            header = None)
events4 = pull_data("9-10-19_9-12-19.data")

data4.columns = ["decay_time","occurance_time"]

data5 = pd.read_csv("Data/9-12-19_9-17-19.data",
            sep = " ",
            header = None)
events5 = pull_data("9-12-19_9-17-19.data")

data5.columns = ["decay_time","occurance_time"]

data6 = pd.read_csv("Data/9-17-19_9-24-19.data",
            sep = " ",
            header = None)
events6 = pull_data("9-17-19_9-24-19.data")

data6.columns = ["decay_time","occurance_time"]

time1 = np.max(data1["occurance_time"]) - np.min(data1["occurance_time"])
time2 = np.max(data2["occurance_time"]) - np.min(data2["occurance_time"])
time3 = np.max(data3["occurance_time"]) - np.min(data3["occurance_time"])
time4 = np.max(data4["occurance_time"]) - np.min(data4["occurance_time"])
time5 = np.max(data5["occurance_time"]) - np.min(data5["occurance_time"])
time6 = np.max(data6["occurance_time"]) - np.min(data6["occurance_time"])

total_time = np.sum((time1/60/60,time2/60/60,time3/60/60,
                     time4/60/60,time5/60/60,time6/60/60))

print("-----")
print("time1 =",time1/60/60,"hours.")
print("time1 # of events =",len(events1[0]))
print("time1 time between events =",time1/len(events1[0]))
print("-----")

print("time2 =",time2/60/60,"hours.")
print("time2 # of events =",len(events2[0]))
print("time2 time between events =",time2/len(events2[0]))
print("-----")

print("time3 =",time3/60/60,"hours.")
print("time3 # of events =",len(events3[0]))
print("time3 time between events =",time3/len(events3[0]))
print("-----")

print("time4 =",time4/60/60,"hours.")
print("time4 # of events =",len(events4[0]))
print("time4 time between events =",time4/len(events4[0]))
print("-----")

print("time5 =",time5/60/60,"hours.")
print("time5 # of events =",len(events5[0]))
print("time5 time between events =",time5/len(events5[0]))
print("-----")

print("time6 =",time6/60/60,"hours.")
print("time6 # of events =",len(events6[0]))
print("time6 time between events =",time6/len(events6[0]))
print("-----")

print("total time =",total_time,"hours.")
print("Total number of events =",len(data))
print("Average time between events =",total_time*60*60/len(data),"seconds")
