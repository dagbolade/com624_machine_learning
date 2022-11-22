# reading data without heading

import csv
import numpy as np


from numpy import loadtxt
from numpy import genfromtxt

with open("venv/pima_indians_diabetes.csv", 'r')as diabetics:

    pima_data = csv.reader(diabetics, delimiter = ',')

    # getting the column header
    diabetics_headers = next(pima_data)
    diabetics_data = list(pima_data)

    # read as numpy array
    diabetics_data = np.array(diabetics_data).astype(float)
print(diabetics_headers)
# data dimension is he number of rows
print(diabetics_data.shape)
print(diabetics_data[:2])


