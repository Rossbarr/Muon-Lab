"""
Created on Tue Sep 17 2019

@author: Barrett and Matt

This document does all the data analysis given the data from either pull_data
or a text file.

We plot the data as a histogram containing counts on the y-axis and event time
on the x-axis.
We fit the data to multiple similar exponential decays.
These fits give us the values we're ultimately looking for.

Running this file will return the parameters for 2 different exponential fits,
as well as a histogram plot with our fits and the data.
"""

import sys
import matplotlib.pyplot as plt        # For plotting.
import numpy as np                     # For numbers and array handling
from scipy.optimize import curve_fit   # For curve fitting
from pull_data import pull_data        # Optional.

#data = pull_data()[0]
data = np.loadtxt('data.txt')[0]
print("length of data: " + str(len(data)))

# The above two commands load in the data. If you're going to use one, comment
# the other.
# We'll now define our different equations for fitting.

def exponential_decay(t,N_0,tau,delta):
	return N_0*np.exp(-t/tau) + delta

def custom_fit(t,A_neg,tau_0,tau_c,A_pos,C):
	return A_neg*np.exp(-t*(1/tau_0+1/tau_c)) + A_pos*np.exp(-t/tau_0)

def neg_muons(t,A_neg,tau_0,tau_c,A_pos,C):
	return A_neg*np.exp(-t*(1/tau_0+1/tau_c))

def pos_muons(t,A_neg,tau_0,tau_c,A_pos,C):
	return A_pos*np.exp(-t/tau_0)

counts, bin_edges, _ = plt.hist(data,bins=50)
# We need the bin_edges to take to fit the data.

time = []       # Initializes the array we'll create for the
for i in range(len(bin_edges)-1):                  # This creates the same
	time.append((bin_edges[i]+bin_edges[i+1])/2.)  # x-axis the histogram uses.
    
    
popt_exp, pcov_exp = curve_fit(exponential_decay, time, counts,
                               p0=(1, 2000, 1),
                               bounds=((0,0,0),
                                       (np.inf,np.inf,np.inf)))

popt_custom, pcov_custom = curve_fit(custom_fit, time, counts, 
					p0=(15, popt_exp[1], 2043, popt_exp[0]/2, popt_exp[2]),
					bounds=(
						(0, 2000, 2023, 0, -np.inf), 
						(np.inf, 2400, 2063, np.inf, np.inf)))
# These commands fit the data to the two functions defined above.

x_fit = np.linspace(100, 17500, 50)                 # This creates the lines
y_exp_fit = exponential_decay(x_fit, *popt_exp)     # we'll use to plot it
y_custom_fit = custom_fit(x_fit, *popt_custom)      # against the data.
y_neg_muons = neg_muons(x_fit, *popt_custom)
y_pos_muons = pos_muons(x_fit, *popt_custom)

# Everything below plots the data.

plt.plot(x_fit,y_exp_fit,color="red",label="Exponential Decay")
plt.plot(x_fit,y_custom_fit,color="green",label="Expanded Fit")
plt.plot(x_fit,y_neg_muons,color="orange",label="Negative Muons")
plt.plot(x_fit,y_pos_muons,color="cyan",label="Positive Muons")
plt.legend()
plt.grid()
plt.title("Histogram of Event Times")
plt.xlabel("Event Time (ns)")
plt.ylabel("Counts")
plt.savefig("Plots/Data.png")

# Everything below returns the values for our fits in print statements.

perr_exp = np.sqrt(np.diag(pcov_exp))
perr_custom = np.sqrt(np.diag(pcov_custom))
print("Fitted histogram with N_0*exp(-t/tau) + delta")
print("N_0 = "+str(popt_exp[0])+"	Error in N_0: "+str(perr_exp[0]))
print("tau = "+str(popt_exp[1])+"     Error in tau: "+str(perr_exp[1]))
print("delta = "+str(popt_exp[2])+"     Error in delta: "+str(perr_exp[2]))
print("\nFitted histogram with A_neg*np.exp(-t*(1/tau_0+1/tau_c)) + A_pos*np.exp(-t/tau_0) + C")
print("A_neg = "+str(popt_custom[0])+"      Error in A_neg: "+str(perr_custom[0]))
print("tau_0 = "+str(popt_custom[1])+"     Error in tau_0: "+str(perr_custom[1]))
print("tau_c = "+str(popt_custom[2])+"     Error in tau_c: "+str(perr_custom[2]))
print("A_pos = "+str(popt_custom[3])+"     Error in A_pos: "+str(perr_custom[3]))
print("C =     "+str(popt_custom[4])+"     Error in C:     "+str(perr_custom[4]))

plt.show()
