import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('numbers.csv')

NUM = df['Num']
NUM_BACK = df['Num_Back']
NUM_SQ = df['Num_SQ']
NUM_BACK_SQ = df['NUM_BACK_SQ']


'''
Separates the data set of groups based on the Power of 10!
'''
def seperate_base_10(df):
	Powers = []
	for i in range(1,10):
		LIST = []
		for item in df:
			if item > 10**i and item < 10**(i+1):
				LIST.append(item)
		Powers.append(LIST)
	return Powers

'''
Function to determine and graph the frequency of their appearence!
How:
For each point, measure distance from last point. Area which have more points will have higher curve?
'''
def clustering(df):
	Clusters = []
	for i in range(1,10):
		Cluster = []
		for item in df:
			if item > 10**i and item < 10**(i+1):
				Cluster.append(item)	
		Clusters.append(Cluster)
	return Clusters

# def frequency(df):
# 	Freq = []
# 	clusters = clustering(df)
# 	for i in range(len(clusters)-1):
# 		d = clusters[i+1][0] - clusters[i][-1]
# 		Freq.append((d, clusters[i][-1], clusters[i+1][0]))
# 	return Freq

# print(len(clustering(NUM)))
# print(frequency(NUM))




def sum_of_digits(x):
	number = []
	for d in str(x):
		number.append(int(d))

	return sum(number)



SUM_NUM = []
SUM_NUM_SQ = []

for i in NUM:
	if sum_of_digits(i)**2 == sum_of_digits(i**2):
		SUM_NUM.append(sum_of_digits(i)**2)
		SUM_NUM_SQ.append(sum_of_digits(i**2)) 

print(SUM_NUM, SUM_NUM_SQ)

plt.plot(SUM_NUM, SUM_NUM_SQ, 'o')
plt.axis('equal')
plt.show()