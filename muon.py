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

possible_gamma_c = np.array([44., 36., 37.3, 36.1, 37., 39.7, 36.5, 30.3, 37.6, 35.2, 37.7, 38.8])*1000.
possible_gamma_c_error = np.array([10., 4., 1.1, 1.0, 7., 1.3, 2., 7., 0.4, 2., 0.7, 0.5])*1000.
gamma_c = (possible_gamma_c/possible_gamma_c_error**2).sum()/(1/(possible_gamma_c_error**2)).sum()/1000000000.
err_gamma_c = np.sqrt(1/(1/(possible_gamma_c_error**2)).sum())/1000000000.
print("gamma_c = " + str(gamma_c))
print("error in gamma_c = " + str(err_gamma_c))

def exponential_decay(t,N_0,tau,delta):
    return N_0*np.exp(-t/tau) + delta

def custom_fit(t,A_neg,tau_0,A_pos,C):
    return (A_neg*np.exp(-t*(1/tau_0+gamma_c)) + A_pos*np.exp(-t/tau_0) + C)

def jacobian(t,A_neg,tau_0,A_pos,C):
    dA_neg = np.exp(-t*(1/tau_0+gamma_c))
    dtau_0 = (A_neg*np.exp(-t*(1/tau_0+gamma_c)) + A_pos*np.exp(-t/tau_0))*t*tau_0**(-2)
    dA_pos = np.exp(-t/tau_0)
    dC = np.ones(len(t))
    return np.transpose([dA_neg, dtau_0, dA_pos, dC])

def neg_muons(t,A_neg,tau_0,A_pos,C):
    return A_neg*np.exp(-t*(1/tau_0+gamma_c)) + C*A_neg/(A_pos+A_neg) 

def pos_muons(t,A_neg,tau_0,A_pos,C):
    return A_pos*np.exp(-t/tau_0) + C*A_pos/(A_pos+A_neg)

counts, bin_edges, _ = plt.hist(data,bins=50)
# We need the bin_edges to take to fit the data.

time = []       # Initializes the array we'll create for the
for i in range(len(bin_edges)-1):                  # This creates the same
    time.append((bin_edges[i]+bin_edges[i+1])/2)  # x-axis the histogram uses.

count_errors = []
for i in counts:
    count_errors.append(np.sqrt(i))
    
print(counts)
popt_exp, pcov_exp = curve_fit(exponential_decay, time, counts,
                               sigma = count_errors,
                               p0=(1, 2000, 1),
                               bounds=((0,0,0),
                                       (np.inf,np.inf,np.inf)))

#print(np.transpose([popt_exp[0]/2, popt_exp[1], popt_exp[0]/2, popt_exp[2]]))
#print(jacobian(time[0],popt_exp[0]/2, popt_exp[1], popt_exp[0]/2, popt_exp[2]))
popt_custom, pcov_custom = curve_fit(custom_fit, time, counts,
                                     sigma = count_errors,
                                     jac = jacobian,
                                     p0=(popt_exp[0]/2, popt_exp[1], popt_exp[0]/2, popt_exp[2]),
                                     bounds=((0, 0, 0, 0), 
                                             (5000., 5000., 5000., 100.)))
# These commands fit the data to the two functions defined above.

# This creates the lines we'll use to plot against the data.
x_fit = np.linspace(0, 20000, 50)                
y_exp_fit = exponential_decay(x_fit, *popt_exp)     
y_custom_fit = custom_fit(x_fit, *popt_custom)      
y_neg_muons = neg_muons(x_fit, *popt_custom)
y_pos_muons = pos_muons(x_fit, *popt_custom)

# Everything below plots the data.
plt.plot(x_fit,y_exp_fit,color="black",label="Exponential Decay")
plt.grid()
plt.title("Histogram of Event Times")
plt.xlabel("Event Time (ns)")
plt.ylabel("Counts")
plt.legend()
plt.savefig("Plots/exp_decay.png")
plt.show()

plt.plot(x_fit,y_exp_fit,color="red",label="Exponential Decay")
plt.plot(x_fit,y_neg_muons,color="orange",label="Negative Muons")
plt.plot(x_fit,y_pos_muons,color="cyan",label="Positive Muons")
plt.plot(x_fit,y_custom_fit,color="black",label="Expanded Fit")
plt.errorbar(time,counts,yerr = count_errors, elinewidth = 5)
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
print("\nFitted histogram with A_neg*np.exp(-t*(1/tau_0+gamma_c)) + A_pos*np.exp(-t/tau_0) + C")
print("tau_0 = "+str(popt_custom[1])+"     Error in tau_0: "+str(perr_custom[1]))
print("A_pos = "+str(popt_custom[2])+"     Error in A_pos: "+str(perr_custom[2]))
print("A_neg = "+str(popt_custom[0])+"      Error in A_neg: "+str(perr_custom[0]))
print("C =     "+str(popt_custom[3])+"     Error in C:     "+str(perr_custom[3]))
print("The charge ratio is",popt_custom[2]/popt_custom[0])

print(pcov_custom)

plt.show()


