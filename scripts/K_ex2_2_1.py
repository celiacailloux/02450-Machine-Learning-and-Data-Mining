# ----------------------------------------------------------------------------
# Imports a matlab file (.mat) of type image data (e.g. heat map) and plots
# it a digit (an observation x_i) using imshow and the same digit in vector
# format (ie. the pixels in a sequence.)
# 
# ML tags: supervised learning
#
# 2021 celiacailloux@gmail.com
#
# exercise 2.1.1 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------

# standard modules
from matplotlib.pyplot import (figure, subplot, imshow, xlabel, title, \
                               yticks, show, cm, savefig)
from scipy.io import loadmat
import numpy as np
import pandas as pd
from os.path import basename, splitext, join
# limit the number of digits to 1
pd.options.display.float_format = '{:,.3f}'.format

# %%
# Index of the digit to display
i = 0

plot_digit_i    = True
save_figure     = True

# %%
# Load Matlab data file to python dict structure
mat_data = loadmat('../Data/zipdata.mat')

# Extract variables of interest
traindata_array = mat_data['traindata']
testdata_array  = mat_data['testdata']


# Convert traindata to dataframe
traindata = pd.DataFrame(traindata_array)
# Determine y and X
y = traindata[[0]] #if instead [0] is used, then it converts from DataFrame to Series
X = traindata.drop(traindata[[0]], axis = 1)

N = len(y) # number of observations, aka number of digits
M = len(X.columns)

# X = traindata['0']
# y = pd.DataFrame(traindata)

X_array = traindata_array[:,1:]
y_array = traindata_array[:,0]

# %%

if plot_digit_i:
    # Visualize the i'th digit as a vector
    f = figure()
    subplot(4,1,4);     # nrows, ncols, index,
    
    J = X.iloc[0,:].values.reshape(1,M)
    imshow(J, extent=(0,256,0,10), cmap=cm.gray_r);
    xlabel('Pixel number');
    title('Digit in vector format');
    yticks([])
    
    # Visualize the i'th digit as an image
    subplot(2,1,1);
    sqrt_M = int(np.sqrt(M))
    I = X.iloc[0,:].values.reshape(sqrt_M,sqrt_M)
    imshow(I, extent=(0,16,0,16), cmap=cm.gray_r);
    title('Digit as an image');
    
    if save_figure:
        # Save figure in the 'figures' directory
        # close('all')  
        exerciseName    = splitext(basename(__file__))[0]    
        saveFigTitle    = exerciseName + '_' + \
            'digit_visualizarion_index_{}'.format(i) 
        saveFigPath     = join('../figures/',saveFigTitle)
        savefig(saveFigPath, dpi = 200)
        print('\'{}\' saved as figure'.format(saveFigTitle))   

print('Ran Exercise K_2.2.1\n')