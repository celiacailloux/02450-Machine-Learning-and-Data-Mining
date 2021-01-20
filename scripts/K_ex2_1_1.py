# ----------------------------------------------------------------------------
# Imports a csv file and classifies each class with a name and an integer
# 
# ML tags: supervised learning, classification
#
# 2021 celiacailloux@gmail.com
#
# exercise 2.1.1 (course 02450 DTU 2018)
# ----------------------------------------------------------------------------



import numpy as np
import xlrd
import pandas as pd
# limit the number of digits to 3
pd.options.display.float_format = '{:,.3f}'.format

# Load xls sheet with data
# file_path = '../data/atm_data_part1.csv'
file_path = '../Data/nanonose.xls'
doc = pd.read_excel(file_path)

# Extract attribute names (1st row, column 4 to 12)
attributeNames  = doc.columns[3:11].tolist()

# Extract class names to python list,
# by removing the 2nd (empty) row and locating the 1st col
# then encode with integers (dict)
classLabels     = doc.drop(doc.index[[0,0]]).iloc[:,0].tolist()
classNames      = sorted(set(classLabels))
classDict       = dict(zip(classNames, range(len(classNames))))

# Extract vector y, convert to pandas DataFrame
y = [classDict[value] for value in classLabels]
y = pd.DataFrame(y, columns = ['class'])

# Preallocate memory, then extract excel data to matrix X
X = doc.drop(doc.index[[0,0]]).reset_index()[attributeNames]
# X = np.empty((90, 8))
# for i, col_id in enumerate(range(3, 11)):
#     X[:, i] = np.asarray(doc.col_values(col_id, 2, 92))

# Compute values of N, M and C.
N = len(y)
M = len(attributeNames)
C = len(classNames)

# Print summary statistic 
print('----------- Summary statistics about data')
print(X.describe())

print('Ran Exercise 2.1.1')