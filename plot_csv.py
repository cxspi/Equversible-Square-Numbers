import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('numbers.csv')

xpoints = df['Num']
ypoints = df['Num_Back']
qxpoints = df['Num_SQ']
qypoints = df['NUM_BACK_SQ']


#y = [10**y for y in range(10**6)]

#plt.ion()
plt.plot(xpoints, ypoints, '.')

# For plotting y=x

# x = [10**x for x in range(1,9)]
# plt.plot(x, x)

#plt.axis('equal')
plt.xscale('log')
plt.yscale('log')
plt.show()
