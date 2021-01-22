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
    show, savefig, close, subplots
from os.path import basename, splitext, join
from itertools import combinations
from math import ceil, floor


# N length of y
# M number of attribute names
# C number of classes

# %%
# Data attributes to be plotted
i = 0
j = 1

##
# Make a simple plot of the i'th attribute against the j'th attribute
# plot(X.iloc[:, i], X.iloc[:, j], 'o')

# %%
# Make another more fancy plot that includes legend, class labels, 
# attribute names, and a title.

# Iterate over all possible 2D combinations of attributes and saveplot
combinations_ij     = list(combinations(range(M),2))
n_combinations_ij   = len(list(combinations_ij))

# nrows, ncols    = 3, ceil(n_combinations_ij/3)
nrows           = ceil(np.sqrt(n_combinations_ij))
ncols           = floor(np.sqrt(n_combinations_ij))
fig, axs        = subplots(nrows = nrows, ncols = ncols)#, sharex=True)
fig.set_figwidth(ncols*3) #no need to determine height
fig.set_figheight(nrows*3)
# fig.subplots_adjust(wspace = 0, hspace=0.5)  

title('NanoNose data')
k = 0
for combination in combinations_ij:
    i = combination[0]
    j = combination[1]

    # iterate through all classes and make a mask
    for c in range(C):
        # select indices belonging to class c:
        # (returns an df with Booleans)
        class_mask      = (y['class']==c) 
        X_attribute_i   = X.iloc[:, i][class_mask]
        X_attribute_j   = X.iloc[:, j][class_mask]
        # plot(X_attribute_i, X_attribute_j, 'o')
        axs.flatten()[k].plot(X_attribute_i, X_attribute_j, 'o', label = classNames[c])
        # axs.flatten()[k].set_aspect('equal')
    

    axs.flatten()[k].set_xlabel(attributeNames[i])
    axs.flatten()[k].set_ylabel(attributeNames[j])
    k += 1
       
    
axs[0,0].legend(bbox_to_anchor=(-1, 1), loc='upper left', borderaxespad=0.)
fig.tight_layout()      

show()
# close('all')  
# Save figure in the 'figures' directory
exerciseName    = splitext(basename(__file__))[0]
# saveFigTitle = exerciseName + '_' + 'attr' + '_' + attributeNames[i] + 'vs' + attributeNames[j]
saveFigTitle    = exerciseName + '_' + 'all_combinations_of_attr'
saveFigPath     = join('../figures/',saveFigTitle)
savefig(saveFigPath, dpi = 200)
print('\'{}\ saved as figure'.format(saveFigTitle))    
print('Ran Exercise 2.1.2 \n')


