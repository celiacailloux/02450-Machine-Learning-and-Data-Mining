# ----------------------------------------------------------------------------
# This script prints the projection of a single observation x_i onto the 
# subspace spanned by V, filtered by the chosen class (b_i = (x_i)_T*V_n = PCi)

# 
# ML tags: PCA, preprocessing data, classification, SVD
#
# SVD: singular value decomposition
# 
# 2021 celiacailloux@gmail.com
#
# 
# exercise 2.1.5 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------

# custom-made modules
from K_ex2_1_1 import y, X, N,M
from K_ex2_1_3 import Z

# %%
# Z is the what is refered to as B in the ML notes.
# Z represents the coordinates of the vector x_i (column data correposinding 
# to a given attribute/column name) when it is projected onto the n-dimensional 
# subspace of V. (i.e. the bottom row in fig. 3.5 in ML notes)

# Read more in K_ex2_1_3 or ML notes

# %%
# choose the integer corresponding to your class, 
# and the desired principal component

class_int   = 4
PC          = 'PC2'

# Projection of water class onto the 2nd principal component.
# water is class = 4
class_mask      = (y['class'] == class_int) 
Z_water         = Z[PC][class_mask] 

print(Z_water)

print('Ran Exercise K_2.1.5')