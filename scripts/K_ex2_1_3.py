# ----------------------------------------------------------------------------
# This script computes the PCAs of X (NxM matrix = Observations x Attributes)
# usking sklearn's decomposition (WITHOUT SCALING) and converts it to a 
# dataframe (Z) AND plots the variance explained ratio / variance explained 
# vs PCAs
# 
# ML tags: Variance Explained, PCA, SVD, preprocessing data, scaling data
# PCA = Principal Component Analysis
# SVD = Singular Value Decomposition
#
# 2021 celiacailloux@gmail.com
#
# Inspiration from 
# https://vitalflux.com/pca-explained-variance-concept-python-example/
# 
# exercise 2.1.3 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------


# (requires data structures from K_ex. 2.2.1)
from K_ex2_1_1 import *
from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, \
    savefig, step, legend, tight_layout, close

from sklearn.metrics import explained_variance_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

close('all')

plot_explained_variance_ratio   = False
save_figure                     = True

# %%

# About PCA and SVD
# It's a LINEAR dimensionality reduction. It uses SVD of the data (X) to 
# project it to a lower dimensional space.
# SVD is an easy way to compute n eigenvectors corresponding to the n LARGEST
# eigenvalues. 
# The n LARGEST eigenvalues preserves the info of the data the best, when 
# reducing dimensionality.
# SVD computes three matrices that together map X: U*Sigma*V_T =X.
# The first n columns of V (= V_T transformed) are by definition the first
# eigenvectors.
# Hence, the projection of single observation x_i (1xN) onto the subspace spanned
# by the FIRST n PC's can therefore be written b_i = (x_i)_T*V_n or
# B = X_tilde*V_n

# %%

# Scale/standardize the datasat (=subtract mean value from data = to center)
'''
# (transform: mean value is subtracted to transform the data to center, AND
# scaled by dividing non-constant features by their standard deviation).
# Note: Scaled data has zero mean and unit variance
# Note: in ML notes transformed X is denoted X_tilde
'''
scaler  = StandardScaler().fit(X)
X_std   = scaler.transform(X)       # = X_tilde
# X_std   = (X-scaler.mean_)/scaler.scale_ #equivalent to the transform funciton

# %%

# Compute B (B = X_tilde*V_n) - a linear dimensionality reduction by SVD 
# (= PCA by computing SVD of Y).
# Note: X is centered but not scaled by default before applying the SVD
pca         = PCA()
pca.fit(X)                          # fits the model with X
B_array     = pca.fit_transform(X)  # fit the model with X and returns X after
                                    # applying dimensionality reduction on X.
B_std_array = pca.fit_transform(X_std)                                        

# Convert X_pca to a dataframe
Z = pd.DataFrame(data = B_array, #B_std_array
                 index = range(0,len(B_array)),
                 columns = ['PC{}'.format(i) for i in range(1, B_array.shape[1]+1)])

# Determine explained variance explained_variance_ratio_ attri
# (=Compute variance explained by principal components)
exp_var_pca     = pca.explained_variance_ratio_ 
# exp_var_pca = pca.explained_variance_ratio_
# exp_var_pca = pca.explained_variance_ 


# Cummulative sum of eigenvalues; this will be used to create a step plot
# for visualizing the variance explained by each PC
cum_sum_eigenvalues = np.cumsum(exp_var_pca)

if plot_explained_variance_ratio:
    # Plot variance explained
    figure()
    plot(range(1,len(exp_var_pca)+1), exp_var_pca, 'o-', label='Individual explained variance')
    plot(range(1,len(cum_sum_eigenvalues)+1), cum_sum_eigenvalues,'o-',label='Cumulative explained variance')
    
    legend(loc='best')
    
    
    title('Variance explained by principal components');
    xlabel('Principal component');
    ylabel('Variance explained');
    tight_layout()
    show()

    if save_figure:
        # Save figure in the 'figures' directory
        exerciseName    = splitext(basename(__file__))[0]
        saveFigTitle    = exerciseName + '_' + 'variance_explained'
        saveFigPath     = join('../figures/',saveFigTitle)
        savefig(saveFigPath, dpi = 200)
        print('\'{}\' saved as figure'.format(saveFigTitle))   

print('Ran Exercise 2.1.3 \n')
