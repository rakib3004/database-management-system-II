import numpy as np

CSVData = open("UserRating.csv")
Array2d_result = np.loadtxt(CSVData, delimiter=",")

print(Array2d_result)