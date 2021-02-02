# ----------------------------------------------------------------------------
# This script computes the PCAs of X (NxM matrix = Observations x Attributes)
# usking sklearn's decomposition (WITHOUT SCALING) and converts it to a 
# dataframe (Z) AND plots the variance explained ratio / variance explained 
# vs PCAs
# 
# ML tags: Variance Explained, PCA, SVD, preprocessing data, scaling data
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

# Scale/standardize the datasat (=subtract mean value from data)
'''
# (transform: mean value is subtracted to transform the data to center, and
# scaled by dividing non-constant features by their standard deviation).
# Note: Scaled data has zero mean and unit variance
'''
scaler  = StandardScaler().fit(X)
X_std   = scaler.transform(X)
# X_std   = (X-scaler.mean_)/scaler.scale_ #equivalent to the transform funciton

# %%

# Linear dimensionality reduction by SVD (=PCA by computing SVD of Y)
# (X is centered but not scaled before applying the SVD)
pca         = PCA()
pca.fit(X)                          # fits the model with X
X_pca       = pca.fit_transform(X)  # fit the model with X and returns X after
                                    # applying dimensionality reduction on X.
X_std_pca   = pca.fit_transform(X_std)                                        

# Convert X_pca to a dataframe
Z = pd.DataFrame(data = X_pca,
                 index = range(0,len(X_pca)),
                 columns = ['PC{}'.format(i) for i in range(1, X_pca.shape[1]+1)])


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
