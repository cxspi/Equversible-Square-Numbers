import numpy
import pandas as pd

def sum_of_digits(x):
	number = []
	for d in str(x):
		number.append(int(d))

	return sum(number)


NUM = []
SUM_NUM = []
SUM_NUM_SQ = []


for i in range(1000):
	if sum_of_digits(i)**2 == sum_of_digits(i**2):
		SUM_NUM.append(sum_of_digits(i))
		SUM_NUM_SQ.append(sum_of_digits(i**2)) 
		NUM.append(i)

data = {'Num': NUM,
        'Num Sum': SUM_NUM,
        'Num Sum SQ': SUM_NUM_SQ,
        }

df = pd.DataFrame(data)

pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)