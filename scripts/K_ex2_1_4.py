# ----------------------------------------------------------------------------
# This script plot the variance explained ratio / variance explained by
# principal components using sklearn modules.
# 
# ML tags: Variance Explained, PCA, SVD, preprocessing data, scaling data
#
# 2021 celiacailloux@gmail.com
#
# 
# exercise 2.1.4 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------

# (requires data structures from ex. 2.2.1 and 2.2.3)
from K_ex2_1_1 import *
from K_ex2_1_3 import *
from submodules.plot_ML_course import subplot_all_combinations

from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, legend

# %%
# Indices of the principal components to be plotted
i = 0
j = 1

print('Type of Z: {}'.format(type(Z)))
print('Shape of Z: {}'.format(Z.shape))

# %%
''' 
Plotting PCAs against each other can explain most of the variance in a data 
set. Below the the ith and jth principal components are plotted against each 
other.
'''

# Plot PCAs of the data against each
f = figure()
title('NanoNose data: PCA')
#Z = array(Z)
for c in range(C):
    # select indices belonging to class c by masking:
    class_mask      = (y['class']==c) 
    Z_i   = X.iloc[:, i][class_mask] # masking a pandas dataframe
    Z_j   = X.iloc[:, j][class_mask]    
    plot(Z_i, Z_j, 'o')
    
legend(classNames)
xlabel(Z.columns.tolist()[i])
ylabel(Z.columns.tolist()[j])
# xlabel('PC{0}'.format(i+1))
# ylabel('PC{0}'.format(j+1))

# # Output result to screen
# show()

subplot_all_combinations(Z, y, 
                         classNames, 
                         attributeNames = Z.columns,
                         n_attributes = M, 
                         n_classes = C,
                         fig_title = 'NanoNose data')

print('Ran Exercise 2.1.4\n')