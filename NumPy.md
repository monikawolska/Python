# Python
# NumPy

	import numpy as np

### ARRAY
#### Creating

	my_array = np.array([1, 2, 3, 4, 5, 6])

#### Creating an Array from a CSV

	csv_array = np.genfromtxt('sample.csv', delimiter=',')
  
## STATISTICS WITH NUMPY
 
### Mean

	np.mean(name_array)
  
#### Calculating the Mean of 2D Arrays
To find the means of each interior array, we specify axis 1 (the “rows”)

	np.mean(name_array, axis=1)
  
To find the means of each index position (i.e, mean of all 1st tosses, mean of all 2nd tosses, …), we specify axis 0 (the “columns”)

	np.mean(name_array, axis=0)
	
### Outliers

sortowanie

	np.sort()
	
### Median
	
	np.median()

### Percentiles

	np.percentile(name_array, number_of_percentile)
	
### Standard Deviation

	np.std(array_name)
	
### Histograms

	from matplotlib import pyplot as plt 
	plt.hist(data)
	plt.show()
	or
	plt.hist(data, bins=5)
	plt.hist(data, bins=5, range=(1, 6))
	
### Normal Distribution

	np.random.normal(0, 1, size=100000)
	
- loc: the mean for the normal distribution
- scale: the standard deviation of the distribution
- size: the number of random numbers to generate

### Binomial Distribution

	np.random.binomial
	
- N: The number of samples or trials
- P: The probability of success
- size: The number of experiments

for example:

	plt.hist(a, range=(0, 10), bins=10, normed=True)
	plt.xlabel('Number of "Free Throws"')
	plt.ylabel('Frequency')
	plt.show()
	
