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
print(np.sum(data))
