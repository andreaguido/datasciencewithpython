# Importing libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generating random data
np.random.seed(42) # Setting the seed for reproducibility
x = np.random.normal(50, 10, 100) # Generating 100 random numbers from a normal distribution with mean 50 and standard deviation 10
y = x + np.random.normal(0, 5, 100) # Generating 100 random numbers from a normal distribution with mean 0 and standard deviation 5 and adding them to x

# Calculating the correlation coefficient and the p-value
r, p = stats.pearsonr(x, y) # Using the Pearson's correlation test
print(f'The correlation coefficient is {r:.2f} and the p-value is {p:.4f}')

# Interpreting the results
if p < 0.05: # Setting the significance level to 0.05
  print('The correlation is statistically significant.')
else:
  print('The correlation is not statistically significant.')

if r > 0: # Checking the sign of the correlation coefficient
  print('The correlation is positive.')
elif r < 0:
  print('The correlation is negative.')
else:
  print('The correlation is zero.')

# Performing a hypothesis test to compare the means of x and y
t, p = stats.ttest_ind(x, y) # Using the independent t-test
print(f'The t-statistic is {t:.2f} and the p-value is {p:.4f}')

# Interpreting the results
if p < 0.05: # Setting the significance level to 0.05
  print('The means of x and y are significantly different.')
else:
  print('The means of x and y are not significantly different.')

