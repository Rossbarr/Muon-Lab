import matplotlib.pyplot as plt
from scipy import stats

data = []
with open("Data/9-10-19_12-6.data","r") as f:
	line = f.readline()
	while line:
		temp = line.split(" ")
		if int(temp[0]) < 20000:
                	data.append(int(temp[0]))
		line = f.readline()

plt.hist(data)
plt.show()
plt.save
