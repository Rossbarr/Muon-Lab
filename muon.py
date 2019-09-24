import sys
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from scipy.optimize import curve_fit
data_name = sys.argv[1]
from pull_data import pull_data

"""
data = []
with open("data.txt","r") as f:
	data = f.readline().split(" ")

"""
data = pull_data()[0]
print("length of data: " + str(len(data)))


def exponential_decay(t,N_0,tau,delta):
	return N_0*np.exp(-t/tau) + delta

def custom_fit(t,A_neg,tau_0,tau_c,A_pos,C):
	return A_neg*np.exp(-t*(1/tau_0+1/tau_c)) + A_pos*np.exp(-t/tau_0)

def neg_muons(t,A_neg,tau_0,tau_c,A_pos,C):
	return A_neg*np.exp(-t*(1/tau_0+1/tau_c))

def pos_muons(t,A_neg,tau_0,tau_c,A_pos,C):
	return A_pos*np.exp(-t/tau_0)

counts, bin_edges, _ = plt.hist(data,bins=50)
time = []
for i in range(len(bin_edges)-1):
	time.append((bin_edges[i]+bin_edges[i+1])/2.)
popt_exp, pcov_exp = curve_fit(exponential_decay, time, counts, p0=(1, 2000, 1),bounds=((0,1800,0),(np.inf,2400,np.inf)))
popt_custom, pcov_custom = curve_fit(custom_fit, 
					time, 
					counts, 
					p0=(15, 2200, 2000, popt_exp[0]/2, popt_exp[2]),
					bounds=(
						(0, 2000, 1800, 0, -np.inf), 
						(np.inf, 2400, 2200, np.inf, np.inf)))

x_fit = np.linspace(100, 17500, 100)
y_exp_fit = exponential_decay(x_fit, *popt_exp)
y_custom_fit = custom_fit(x_fit, *popt_custom)
y_neg_muons = neg_muons(x_fit, *popt_custom)
y_pos_muons = pos_muons(x_fit, *popt_custom)

plt.plot(x_fit,y_exp_fit,color="red",label="Exponential Decay")
plt.plot(x_fit,y_custom_fit,color="green",label="Custom Fit")
plt.plot(x_fit,y_neg_muons,color="orange",label="Negative Muons")
plt.plot(x_fit,y_pos_muons,color="cyan",label="Positive Muons")
plt.legend()
plt.xlabel("Decay Time (ns)")
plt.ylabel("Counts")
plt.savefig("Plots/"+data_name+".png")

perr_exp = np.sqrt(np.diag(pcov_exp))
perr_custom = np.sqrt(np.diag(pcov_custom))
print("Fitted histogram with N_0*exp(-t/tau)+delta")
print("N_0 = "+str(popt_exp[0])+"	Error in N_0: "+str(perr_exp[0]))
print("tau = "+str(popt_exp[1])+"     Error in tau: "+str(perr_exp[1]))
print("delta = "+str(popt_exp[2])+"     Error in delta: "+str(perr_exp[2]))
print("\nFitted histogram with A_neg*np.exp(-t*(1/tau_0+1/tau_c))+A_pos*np.exp(-t/tau_0)")
print("A_neg = "+str(popt_custom[0])+"	Error in A_neg: "+str(perr_custom[0]))
print("tau_0 = "+str(popt_custom[1])+"     Error in tau_0: "+str(perr_custom[1]))
print("tau_c = "+str(popt_custom[2])+"     Error in tau_c: "+str(perr_custom[2]))
print("A_pos = "+str(popt_custom[3])+"     Error in A_pos: "+str(perr_custom[3]))
print("C = "+str(popt_custom[4])+"     Error in C: "+str(perr_custom[4]))

plt.show()
