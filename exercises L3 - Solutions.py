# # Exercises Lecture 3

# # Card and Krueger (1994) available <a href="https://davidcard.berkeley.edu/papers/njmin-aer.pdf">here</a>
# 
# The data data-difference-in-differences.csv is based on the original data provided by Card and Krueger (1994). The original data public.dat and can be downloaded at the MHE Data Archive. 
# 
# Variables have been renamed to decrease cognitive load. Rows are 410 fast-food restaurants in New Jersey and eastern Pennsylvania, interviewed in February/March 1992 and November/December 1992 (see Card and Krueger 1994, Tab. 1, p. 774). 

# cleaning memory
for v in dir(): del globals()[v]
pass

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Datasets/data-difference-in-differences.csv", header=0)
df.head()


# Read me: 
# 
# Below variables that are in the example dataset.
# 
# - y_ft_employment_before: Full time equivalent employment before treatment [Outcome]
# - y_ft_employment_after: Full time equivalent employment after treatment [Outcome]
# - d_nj: 1 if New Jersey; 0 if Pennsylvania (treatment variable) [Treatment]
# - x_co_owned: If owned by company = 1
# - x_southern_nj: If in southern NJ = 1
# - x_central_nj: If if in central NJ = 1
# - x_northeast_philadelphia: If in Pennsylvania, northeast suburbs of Philadelphia = 1
# - x_easton_philadelphia: If in Pennsylvania, Easton = 1
# - x_st_wage_before: Starting wage (dollar/hr) before treatment
# - x_st_wage_after: Starting wage (dollar/hr) after treatment
# - x_burgerking: If Burgerking = 1
# - x_kfc: If KFC = 1
# - x_roys: If Roys = 1
# - x_wendys: If Wendys = 1
# - x_closed_permanently: Closed permanently after treatment

# # Data cleaning

# ## 1. Add a string variable indicating whehther NJ or PA

df["state"] = np.where(df["d_nj"]==1 ,"NJ","PA")
df.head()


# # Statistics
# 
# Consider table 3, the first three columns (stores by state)

# ## 1. Reproduce figures in Table 3, 1st and 2nd rows, first two columns Stores by state
# Employment by state, before and after

df_tab3= df.loc[:,["state","y_ft_employment_before","y_ft_employment_after"]].groupby("state").mean().T
df_tab3

# ## 2. Compute 3. row

## one way
import copy
df_tab3row = (df_tab3.T)
df_tab3row["diff_ymean"]= df_tab3row["y_ft_employment_after"]-df_tab3row["y_ft_employment_before"]
df_tab3row["diff_ymean"]

# ## 3. Compute the average change in wages after the introduction of the law in e
# 
# the change is given by MeanWage|treatment=1 - Mean|treatment=0



# # Visualizing

# ## 1. plot histogram of main variables of interest (wages and employment)
# 
# you can do this in a unique plot or 4 sep ones

df_main= df.loc[:,["x_st_wage_before","x_st_wage_after","y_ft_employment_before","y_ft_employment_after"]]
df_main.hist()


# ## 2. Reproduce figure 1  (p.777)
# Q: What does the Figure display and what do the authors want to show?

w_before_nj = df.loc[df["d_nj"]==1, ["x_st_wage_before"]]
w_before_pa = df.loc[df["d_nj"]==0, ["x_st_wage_before"]]
x_bins = np.arange(4.20,5.60,0.1)

plt.hist(w_before_nj, x_bins, alpha=0.5, label='NJ', density=True)
plt.hist(w_before_pa, x_bins, alpha=0.5, label='PA', density=True)


w_before_nj = df.loc[df["d_nj"]==1, ["x_st_wage_after"]]
w_before_pa = df.loc[df["d_nj"]==0, ["x_st_wage_after"]]
x_bins = np.arange(4.20,5.60,0.1)
plt.hist(w_before_nj, x_bins, alpha=0.5, label='NJ', density=True)
plt.hist(w_before_pa, x_bins, alpha=0.5, label='PA', density=True)


# ## 3. Plot the change in employment before and after the introduction, by treatment
# 
# the plot used is a line plot of average values of y_ft_employment

df_diff_diff = df.groupby("state").mean().T.loc[["y_ft_employment_before","y_ft_employment_after"]]
df_diff_diff.plot()
df_diff_diff

