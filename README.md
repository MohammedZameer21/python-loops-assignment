# python-loops-assignment
Question: Temperature Data Processing

Task 1: Create an Array and Basic Math
Problem: A weather station recorded temperatures (in Celsius) for 5 days: 22, 25, 28, 24, 26

Requirements:
Create a NumPy array called temps_celsius with these values
Convert all temperatures to Fahrenheit using: F = C × 1.8 + 32
Print both Celsius and Fahrenheit arrays
Calculate the average temperature in Fahrenheit

Example Output:
Celsius: [22 25 28 24 26]
Fahrenheit: [71.6 77.  82.4 75.2 78.8]
Average Fahrenheit: 77.0

Constraints:
Use NumPy array operations (no loops)
Round average to 1 decimal place


Task 2: Array Shape and Statistics
Problem: You have 12 test scores stored in an array: np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

Requirements:
Print the shape of this array
Find the total number of elements in the array
Calculate the highest score
Calculate the lowest score
Calculate the range (difference between highest and lowest)

Example Output:
Shape: (12,)
Total elements: 12
Highest score: 95
Lowest score: 76
Range: 19

Constraints:
Use np.max() and np.min() functions
Use .shape attribute


Task 3: Performance Comparison
Problem: Compare NumPy array performance against Python lists for a simple calculation.

Requirements:
Create a NumPy array with numbers from 1 to 50000 using np.arange(1, 50001)
Create a Python list with the same numbers using list(range(1, 50001))
Calculate the sum using NumPy's np.sum()
Calculate the sum using Python's sum()
Measure and print the time taken for both operations
Calculate how many times faster NumPy is

Example Output:
NumPy sum: 1250025000
Python sum: 1250025000
NumPy time: 0.0002 seconds
Python time: 0.0031 seconds
NumPy is 15.5x faster

Constraints:
Use time.time() for timing
Both sums must match
Format time to 4 decimal places
