# ----------------------------------------------------------------------------
# Plots 2 unnormalized attributes against each and colors with the 
# classification. Data imported (and structured) in K_ex2_1_1
#
# i -- attribute plottet on the 1st axis
# j -- attribute plottet on the 2nd axis
# 
# ML tags: supervised learning, classification
#
# 2021 celiacailloux@gmail.com
#
# exercise 2.1.2 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------

# Imports the numpy, xlrd and pandas package, then runs the ex2_1_1 code
from K_ex2_1_1 import *
# (requires data structures from ex. 2.1.1)

from matplotlib.pyplot import figure, plot, title, legend, xlabel, ylabel, \
    show, savefig, close
from os.path import basename, splitext, join
from itertools import combinations


# N length of y
# M number of attribute names
# C number of classes

# Data attributes to be plotted
i = 0
j = 1

##
# Make a simple plot of the i'th attribute against the j'th attribute
# Notice that X is of matrix type (but it will also work with a numpy array)
# X = np.array(X) #Try to uncomment this line
plot(X.iloc[:, i], X.iloc[:, j], 'o')

# %%
# Make another more fancy plot that includes legend, class labels, 
# attribute names, and a title.
f = figure()
title('NanoNose data')

# iterate through all classes and make a mask
for c in range(C):
    # select indices belonging to class c:
    # (returns an df with Booleans)
    class_mask = (y['class']==c) 
    X_attribute_i = X.iloc[:, i][class_mask]
    X_attribute_j = X.iloc[:, j][class_mask]
    plot(X_attribute_i, X_attribute_j, 'o')

legend(classNames)
xlabel(attributeNames[i])
ylabel(attributeNames[j])

# Save figure in the 'figures' directory
exerciseName = splitext(basename(__file__))[0]
saveFigTitle = exerciseName + '_' + 'attr' + '_' + attributeNames[i] + 'vs' + attributeNames[j]
saveFigPath = join('../figures/',saveFigTitle)
savefig(saveFigPath)

# Output result to screen
# show()
close('all')

# Iterate over all possible 2D combinations of attributeNames
for combination in combinations(range(M),2):
    print(combination)
print('Ran Exercise 2.1.2')