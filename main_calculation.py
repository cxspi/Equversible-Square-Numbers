import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Starting...")

# How I'd probably write it:
def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)

def back_square(x):
	pass

def num_back(x):
	number = []
	for d in str(x):
		number.append(int(d))

	number.reverse()
	
	return magic(number)

NUM = []
NUM_BACK = []
NUM_SQ = []
NUM_BACK_SQ = []

for x in range(10,10**9): 
	if x**2 == num_back(num_back(x)**2):
		#print("yo", x, num_back(x),num_back(num_back(x)**2), num_back(x)**2)
		NUM.append(x)
		NUM_BACK.append(num_back(x))
		NUM_SQ.append(x**2)
		NUM_BACK_SQ.append(num_back(x)**2)

data = {'Num': NUM,
        'Num_Back': NUM_BACK,
        'Num_SQ': NUM_SQ,
        'NUM_BACK_SQ': NUM_BACK_SQ
        }


df = pd.DataFrame(data)
pd.set_option("display.max_rows", None, "display.max_columns", None)
df.to_csv('numbers_10E12.csv')

print (df)

xpoints = np.array(NUM)
ypoints = np.array(NUM_BACK)

plt.plot(xpoints, ypoints, 'o')
plt.show()

print("Done!")
