"""
Created on Tue Sep 17 2019

@author: Barrett and Matt

The document does the data analysis required for question 13 in the recommended
student excersizes from the manual.

Running this reports the mean and variance of how many decays succeeded when
binned in sizes of 50.

That is, we bin all the data into 50 arrays.
We count how many data points are less than tau_0 and add that to a tally
of successes.
Each bin will have around 31 successes.

We plot a histogram of the distribution of bin succession number. 
"""

import sys
import matplotlib.pyplot as plt        # For plotting.
import numpy as np                     # For numbers and array handling

#data = pull_data()[0]
data = np.loadtxt("data.txt")[0]
print("length of data: " + str(len(data)))

# The above two commands load in the data. If you're going to use one, comment
# the other.

n=0
tau_0 = 2200
averages = []
while 50*(n+1) < len(data):
	average_successes = 0
	for i in data[(50*int(n)):(50*int(n+1))]:
		if i < tau_0:
			average_successes += 1
	averages.append(average_successes)
	n += 1

mean = np.sum(averages)/len(averages)

print('The mean is ', mean)

values = np.zeros_like(averages)
for i in range(len(averages)):
    values[i] = (averages[i] - mean)**2
    
variance = np.sum(values)/len(averages)

print('The variance is ', variance)
plt.title("Histogram of Data")
plt.xlabel("Number of Success in Bins of 50")
plt.ylabel("Counts")
plt.grid()
plt.hist(averages,
         bins=[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
               29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
               color='green')
plt.savefig("Plots/Question_13")
plt.show()
