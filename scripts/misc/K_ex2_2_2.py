# ----------------------------------------------------------------------------
# This script computes and plots the variance explained and projects data 
# onto principal component space. It also plots the a reconstruction of the
# data to its original space with the chosen number of principal components.
# 
# ML tags: Variance Explained, Inverse Transformation, PC
#
# 2021 celiacailloux@gmail.com
#
# 
# exercise 2.2.2 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------

# custom-made modules
from submodules.file_manage_pickle import save_as_pickle, get_saved_pickle
from submodules.plot_ML_course import save_figure_as_script_title, save_figure_w_comment


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

plot_variance_explained = False
plot_PCi_vs_PCj         = False
plot_PC_reconstruction  = True 
save_figure             = True

# Selection of classes, aka in this case digits to include in analysis and
# plotting (to include all, n = range(10)) and number of classes (C)
c = [0,1]
C = len(c)
# Number of principal components for reconstruction and number of digits 
# (observations N) to visualize, aka number of digits
K = 16
n = range(6)

# exerciseName = splitext(basename(__file__))[0] # name of script
exerciseName = 'test'

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
    
# Classes represented by values, strings and paired in a dict
classValues     = c
classNames      = [str(class_i) for class_i in c]
classDict       = dict(zip(classNames,classValues))

#%%
# Select subset of digits classes (c) to be inspected, by
# making a mask of booleans
class_mask  = y['class'].isin(c) # pandas masking with regards to a list
X           = X[class_mask] # masking rows in pandas
y           = y[class_mask]
# number of observations of the subset and number of pixels (sqrt_Mxsqrt_M)
N, M        = X.shape
sqrt_M = int(np.sqrt(M))

# Get the variance explained and the data projected onto principal component 
# space (B or Z)
pca             = PCA(n_components = K).fit(X)
exp_var_pca     = pca.explained_variance_ratio_ 
B_array         = pca.fit_transform(X)
Z = pd.DataFrame(data = B_array, #B_std_array
                 index = range(0,len(B_array)),
                 columns = ['PC{}'.format(i) for i in range(1, K+1)])#B_array.shape[1]+1)])
X_proj          = pd.DataFrame(pca.inverse_transform(Z), columns = X.columns)
# %%

if plot_variance_explained:
    # Plot variance explained
    figure()
    plot(range(1, K+1), exp_var_pca,'o-')# percentage of variance explained
    # plot(pca.explained_variance_, 'o-')
    title('Variance explained by principal components\nDigits data');
    xlabel('Principal component');
    ylabel('Variance explained value');
    if save_figure:
        save_figure_as_script_title(__file__,
                                    comment = \
                                        'USPS_handwritten_Variance_explained_by_PC_w_{}_PCs'.format(K))
        

if plot_PCi_vs_PCj:
    # Plot PCA of the data
    f = figure()
    title('pixel vectors of handwr. digits projected on PCs')
    for _class in c:
        # select indices belonging to class c:
        class_mask_plot = (y['class'] == _class).reset_index(drop = True)
        plot(Z['PC1'][class_mask_plot], Z['PC2'][class_mask_plot], 'o')
    legend(classNames)
    xlabel('PC1')
    ylabel('PC2')
    if save_figure:
            save_figure_as_script_title(__file__,
                                        comment = \
                                            'USPS_handwritten_digits_PC1vsPC2')    
if plot_PC_reconstruction:
    # Visualize the reconstructed data (X_reconstructured) from the first K
    # principal components by selectecting D number of observations (or D
    # number of random observations x_idx)
    figure(figsize=(10,3))
    D = len(n)
    for d in range(D):
        x_idx = np.random.randint(0,N)
        subplot(2, D, d+1)
        
        # I = X.iloc[x_idx,:].values.reshape(16,16)
        I = X.iloc[d,:].values.reshape(sqrt_M,sqrt_M)        
        imshow(I, cmap=cm.gray_r)
        title('Original')
        
        subplot(2, D, D+d+1)
        # I = np.reshape(X_proj[d,:], (sqrt_M,sqrt_M))
        I = X_proj.iloc[d,:].values.reshape(sqrt_M,sqrt_M) 
        imshow(I, cmap=cm.gray_r)
        title('Reconstr.')
    if save_figure:
        save_figure_as_script_title(file_path = None, 
                                    exerciseName = exerciseName,
                                    comment = \
                                        'USPS_handwritten_original_vs_reconstructed_digit_w_{}_PCs'.format(K))    

        save_figure_w_comment(figTitle = exerciseName,
                              comment = 'test')#\
        # 'USPS_handwritten_original_vs_reconstructed_digit_w_{}_PCs'.format(K))                    
    

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