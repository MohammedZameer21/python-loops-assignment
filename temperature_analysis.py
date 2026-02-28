#Task 1:

import numpy as np
import time

#Create NumPy array with Celsius temperatures
temps_celsius = np.array([22, 25, 28, 24, 26])

#   Converting to Fahrenheit
temps_fahrenheit = temps_celsius * 1.8 + 32

#Printing both arrays
print("Celsius:",temps_celsius)
print("Fahrenheit:",temps_fahrenheit)

#  Calculate average temperature in Fahrenheit
avg_fahrenheit = sum(temps_fahrenheit)/len(temps_fahrenheit)

# Round to 1 decimal place
print("Average Fahrenheit:",round(avg_fahrenheit,1))

#Output1:

#Celsius: [22 25 28 24 26]
#Fahrenheit: [71.6 77.  82.4 75.2 78.8]
#Average Fahrenheit: 77.0


#Task 2:

#creating numpy arry
scores=np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

#printing shape
print("Shape:",scores.shape)

#Total elements of arr
print("Total elements:",len(scores))

#Highest score
print("Highest score:",np.max(scores))

#Lowest score
print("Lowest score:",np.min(scores))

#Difference between highest and lowest score
print("Range:",np.max(scores)-np.min(scores))

#Output2:

#Shape: (12,)
#Total elements: 12
#Highest score: 95
#Lowest score: 76
#Range: 19


#Task 3:

#creating numpy array
n_arr = np.arange(1,50001)

#creating  List
l_arr = list(range(1,50001))

#sum and calculating time
st = time.time()
np.sum(n_arr)
en = time.time()

st1 = time.time()
sum(l_arr)
en1 = time.time()

print("Numpy sum:",np.sum(n_arr))
print("Python sum:",sum(l_arr))

#Printing time to calculate sum
ntime = round(en-st,4)
ltime = round(en1-st1,4)
print("Numpy time:",ntime)
print("Python time:",ltime)

#How much faster is Numpy
speed = ltime/ntime
print(f"Numpy is {speed:.1f}x faster")

#Output3:

#Numpy sum: 1250025000
#Python sum: 1250025000
#Numpy time: 0.0001
#Python time: 0.0004
#Numpy is 4.0x faster