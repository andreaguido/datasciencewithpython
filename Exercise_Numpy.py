import os
import numpy as np
os.getcwd()
os.chdir()
data = np.genfromtxt(fname="2021)_Baseball_Teams.csv",delimiter=";", skip_header = 1)

data.shape

# Hints before you go:
# save columns that you need to use (numpy has no idea of what a dataframe is)
NY = data[:,1]
BO = data[:,2]
CS = data[:,3]
YR= data[:,0]

## Goals:

# 1 create a function that prints summary statistics (median, average and SD) of Runs scored of all teams 
def stats(col):
  print('Mean is: ', round(np.nanmean(col),1))
  print('Median is: ', round(np.nanmedian(col),1))
  print('Standard dev is: ', round(np.nanstd(col),1))
  pass

stats(NY)

def stats(data):
  print("Team        NY      |   BO     |   CS   ")
  print('Mean       ', round(np.nanmean(data[:1]),1), " | ", round(np.nanmean(data[:2]),1) ," | ",round(np.nanmean(data[:3]),1))
  print('Med.       ', round(np.nanmedian(data[:1]),1), " | ", round(np.nanmedian(data[:2]),1) ," | ",round(np.nanmedian(data[:3]),1))
  print('Std.       ', round(np.nanstd(data[:1]),1), " | ", round(np.nanstd(data[:2]),1) ," | ",round(np.nanstd(data[:3]),1))
  pass

stats(data)
# 2 now include in the function the possibility to select a range of years and provide same statistics

def stats_year(yearI, yearE, team):
  yI = np.where(YR==yearI)
  yE = np.where(YR==yearE)
  dt=team[yI[0][0]:yE[0][0]+1]
  stats(dt)

stats_year(yearE = 2010, col = NY, yearI =1992)


def stats_year_david(yearI, yearE, team):
  yI = np.where(YR>=yearI)
  yE = np.where(YR<=yearE)
  third = np.intersect1d(yI,yE)
  #dt=team[yI[0][0]:yE[0][0]+1]
  stats(team[third])

# 3 create a function to define who did more runs between two given teams

# 4 create a function to compute moving averages over the time series

# 5 t-test between two teams run scores
