import sys
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from scipy.optimize import curve_fit
from pull_data import pull_data

"""
data = []
with open("data.txt","r") as f:
	data = f.readline().split(" ")

"""
data = pull_data()[0]
print("length of data: " + str(len(data)))

n=0
tau_0 = 2213.095735211033
averages = []
while 50*(n+1) < len(data):
	average_successes = 0
	for i in data[(50*int(n)):(50*int(n+1))]:
		if i < tau_0:
			average_successes += 1
	averages.append(average_successes)
	n += 1
print(averages)	
print(np.sum(averages)/len(averages))
plt.hist(averages,bins=[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
plt.show()
