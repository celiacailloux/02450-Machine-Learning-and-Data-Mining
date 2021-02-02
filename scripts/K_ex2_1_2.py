# ----------------------------------------------------------------------------
# Plots all combinations of unnormalized attributes/features against each and 
# colors with respect to the classification. 
# Data imported (and structured) in K_ex2_1_1
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

# custom-made modules
from submodules.plot_ML_course import subplot_all_combinations
# Imports the numpy, xlrd and pandas package, then runs the ex2_1_1 code
from K_ex2_1_1 import *
# (requires data structures from ex. 2.1.1)

# standard modules

from os.path import basename, splitext, join

# N length of y / number of attributes
# M number of attribute names
# C number of classes

# %%
# Data attributes to be plotted
# i = 0
# j = 1

##
# Make a simple plot of the i'th attribute against the j'th attribute
# plot(X.iloc[:, i], X.iloc[:, j], 'o')

# %%
# Plot all combinations of features / attributes
# including legend, class labels, attribute names, and a title.


subplot_all_combinations(X, y, 
                         classNames, attributeNames,
                         n_attributes = M, 
                         n_classes = C,
                         fig_title = 'NanoNose data')

# Save figure in the 'figures' directory
# close('all')  
exerciseName    = splitext(basename(__file__))[0]    
saveFigTitle    = exerciseName + '_' + 'all_combinations_of_attr' 
saveFigPath     = join('../figures/',saveFigTitle)
savefig(saveFigPath, dpi = 200)
print('\'{}\ saved as figure'.format(saveFigTitle))   
# print('Ran Exercise 2.1.2 \n')


