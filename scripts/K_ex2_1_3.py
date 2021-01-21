# ----------------------------------------------------------------------------
# This script plot the variance explained ratio / variance explained by
# principal components using sklearn modules
# 
# ML tags: Variance Explained, PCA, SVD, 
#
# 2021 celiacailloux@gmail.com
#
# inspiration from https://vitalflux.com/pca-explained-variance-concept-python-example/
# 
# exercise 2.1.3 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------


# (requires data structures from K_ex. 2.2.1)
from K_ex2_1_1 import *
from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, \
    savefig, step, legend, tight_layout

from sklearn.metrics import explained_variance_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

save_figure = True

# %%

''' 
when scaling the dataset, the explained variance varies from the course script
where linear algebra is excecuted - you should follow up on this step. What 
does the StandardScaler() do?
'''

# Scale the datasat (=subtract mean value from data)
sc      = StandardScaler()
sc.fit(X)
X_std   = sc.transform(X)

# %%

# Determine transformed features (=PCA by computing SVD of Y)
pca     = PCA()
# X_pca   = pca.fit_transform(X_std)    # see note in previous section
X_pca   = pca.fit_transform(X)

# Determine explained variance explained_variance_ratio_ attri
# (=Compute variance explained by principal components)
exp_var_pca = pca.explained_variance_ratio_
# exp_var_pca = pca.explained_variance_


# Cummulative sum of eigenvalues; this will be used to create a step plot
# for visualizing the variance explained by each PC
cum_sum_eigenvalues = np.cumsum(exp_var_pca)

# Plot variance explained
figure()
plot(range(0,len(exp_var_pca)), exp_var_pca, 'o-', label='Individual explained variance')
plot(range(0,len(cum_sum_eigenvalues)), cum_sum_eigenvalues,'o-',label='Cumulative explained variance')

legend(loc='best')


title('Variance explained by principal components');
xlabel('Principal component Index');
ylabel('Variance explained');
tight_layout()
show()

if save_figure:
    # Save figure in the 'figures' directory
    exerciseName    = splitext(basename(__file__))[0]
    saveFigTitle    = exerciseName + '_' + 'variance_explained'
    saveFigPath     = join('../figures/',saveFigTitle)
    savefig(saveFigPath, dpi = 200)
    print('\'{}\ saved as figure'.format(saveFigTitle))   

print('Ran Exercise 2.1.3')
