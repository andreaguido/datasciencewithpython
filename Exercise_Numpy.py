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
