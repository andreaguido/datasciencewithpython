import os
import numpy as np
os.getcwd()
os.chdir()
data = np.genfromtxt(fname="2021_Baseball_Teams.csv",delimiter=";", skip_header = 1)

data.shape

# Hints before you go:
# save columns that you need to use (numpy has no idea of what a dataframe is)
NY = data[:,1]
BO = data[:,2]
CS = data[:,3]
YR= data[:,0]

## Goals:

# 1 create a function that prints summary statistics (median, average and SD) of Runs scored of all teams 

# 2 now include in the function the possibility to select a range of years and provide same statistics

# 3 create a function to define who did more runs between two given teams

# 4 create a function to compute moving averages over the time series

# 5 t-test between two teams run scores
