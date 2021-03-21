# ----------------------------------------------------------------------------
# This script plots all combinations of PCAs against each other
# 
# ML tags: PCA, preprocessing data
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

plot_single_of_PCs_ivsj         = True
plot_all_combinations_of_PCAs   = False

save_figure                     = True 

# %% 

# For more on PCA go to K_ex2_1_3

# %%

# Single plot of PC_i and PC_j
if plot_single_of_PCs_ivsj:
    # Indices of the principal components to be plotted
    i = 0
    j = 1
    
    # Plot PCAs of the data against each
    f = figure()
    title('NanoNose data: PCA')
    #Z = array(Z)
    for c in range(C):
        # select indices belonging to class c by masking:
        class_mask      = (y['class']==c) 
        Z_i   = X.iloc[:, i][class_mask] # masking columns in a pandas dataframe
        Z_j   = X.iloc[:, j][class_mask]    
        plot(Z_i, Z_j, 'o')
        
    legend(classNames)
    xlabel(Z.columns.tolist()[i])
    ylabel(Z.columns.tolist()[j])
    if save_figure:
        # Save figure in the 'figures' directory
        # close('all')  
        exerciseName    = splitext(basename(__file__))[0]    
        saveFigTitle    = exerciseName + '_' + '_PC_{0}vs{1}'.format(i+1,j+1) 
        saveFigPath     = join('../figures/',saveFigTitle)
        savefig(saveFigPath, dpi = 200)
        print('\'{}\' saved as figure'.format(saveFigTitle))   

# %% 
# About Z

# print('Type of Z: {}'.format(type(Z)))
# print('Shape of Z: {}'.format(Z.shape))

# %%

if plot_all_combinations_of_PCAs:
    ''' 
    Plotting PCAs against each other can explain most of the variance in a data 
    set. Below the the ith and jth principal components are plotted against each 
    other.
    '''
    
    
    
    # plot all combinations of PCAs with each other
    subplot_all_combinations(Z, y, 
                             classNames, 
                             plot_labels = Z.columns,
                             n_attributes = M, 
                             n_classes = C,
                             fig_title = 'NanoNose data')
    if save_figure:
        # Save figure in the 'figures' directory
        # close('all')  
        exerciseName    = splitext(basename(__file__))[0]    
        saveFigTitle    = exerciseName + '_' + 'all_combinations_of_PCAs' 
        saveFigPath     = join('../figures/',saveFigTitle)
        savefig(saveFigPath, dpi = 200)
        print('\'{}\' saved as figure'.format(saveFigTitle))   

print('Ran Exercise K_2.1.4\n')