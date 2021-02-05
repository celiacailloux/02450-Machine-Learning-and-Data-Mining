# ----------------------------------------------------------------------------
# This script ...
# 
# ML tags: Variance Explained, 
#
# 2021 celiacailloux@gmail.com
#
# 
# exercise 2.2.2 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------

# custom-made modules
from submodules.file_manage_pickle import save_as_pickle, get_saved_pickle
from submodules.plot_ML_course import save_figure_as_script_title


# standard modules
from matplotlib.pyplot import (figure, subplot, plot, xlabel, ylabel, title, \
                               yticks, show,legend,imshow, cm)
from scipy.io import loadmat
from os.path import basename, splitext, join
# import scipy.linalg as linalg
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


# %%
import_data             = False

plot_variance_explained = True
plot_PCAi_vs_PCAj       = False 
save_figure             = True 

exerciseName = splitext(basename(__file__))[0] # name of script

# %%
if import_data:
    from K_ex2_2_1 import X, y
    data = {'X' : X, 
            'y' : y}
    save_as_pickle(pkl_data = data, pkl_name = 'data')
else:
    data = get_saved_pickle(pkl_name = 'data')
    
    X = data['X']
    y = data['y']     
    

# Selection of classes, aka digits to include in analysis (to include all, 
# n = range(10) )
n = [0,1]
# Number of principal components for reconstruction
K = 16
# Digits to visualize, aka number of visualizations
nD = range(6); 


# # Load Matlab data file to python dict structure
# # and extract variables of interest
# traindata = loadmat('../Data/zipdata.mat')['traindata']
# X = traindata[:,1:]
# y = traindata[:,0]

# Number of observations (N) and attributes (M)
# and number of classes (C)
N, M = X.shape
C = len(n)

# Classes represented by values, strings and paired in a dict
classValues     = n
classNames      = [str(num) for num in n]
classDict       = dict(zip(classNames,classValues))


# Select subset of digits classes (n) to be inspected, by
# making a mask of booleans
class_mask = y['class'].isin(n) # pandas masking with regards to a list
X = X[class_mask] # masking rows in pandas
y = y[class_mask]
# number of observations of the subset n (e.g. the digits n = [0,1])
N = X.shape[0]

# Get the variance explained
pca         = PCA().fit(X)
# pca.fit(X)

# Get the project data onto principal component space
exp_var_pca     = pca.explained_variance_ratio_ 
B_array         = pca.fit_transform(X)
Z = pd.DataFrame(data = B_array, #B_std_array
                 index = range(0,len(B_array)),
                 columns = ['PC{}'.format(i) for i in range(1, B_array.shape[1]+1)])

if plot_variance_explained:
    # Plot variance explained
    figure()
    plot(exp_var_pca,'o-')
    title('Variance explained by principal components\nDigits data');
    xlabel('Principal component');
    ylabel('Variance explained value');
    if save_figure:
        save_figure_as_script_title(exerciseName,
                                    comment = \
                                        'USPS_handwritten_Variance_explained_by_PC')
        

if plot_PCAi_vs_PCAj:
    # Plot PCA of the data
    f = figure()
    title('pixel vectors of handwr. digits projected on PCs')
    for c in n:
        # select indices belonging to class c:
        class_mask_plot = (y['class'] == c).reset_index(drop = True)
        plot(Z['PC1'][class_mask_plot], Z['PC2'][class_mask_plot], 'o')
    legend(classNames)
    xlabel('PC1')
    ylabel('PC2')
    if save_figure:
            save_figure_as_script_title(exerciseName,
                                        comment = \
                                            'USPS_handwritten_digits_PC1vsPC2')    



# # Visualize the reconstructed data from the first K principal components
# # Select randomly D digits.
# figure(figsize=(10,3))
# W = Z[:,range(K)] @ V[:,range(K)].T
# D = len(nD)
# for d in range(D):
#     digit_ix = np.random.randint(0,N)
#     subplot(2, D, d+1)
#     I = np.reshape(X[digit_ix,:], (16,16))
#     imshow(I, cmap=cm.gray_r)
#     title('Original')
#     subplot(2, D, D+d+1)
#     I = np.reshape(W[digit_ix,:]+X.mean(0), (16,16))
#     imshow(I, cmap=cm.gray_r)
#     title('Reconstr.');
    

# # Visualize the pricipal components
# figure(figsize=(8,6))
# for k in range(K):
#     N1 = np.ceil(np.sqrt(K)); N2 = np.ceil(K/N1)
#     subplot(N2, N1, k+1)
#     I = np.reshape(V[:,k], (16,16))
#     imshow(I, cmap=cm.hot)
#     title('PC{0}'.format(k+1));

# # output to screen
# show()

# '''
# print('Ran Exercise 2.2.2')