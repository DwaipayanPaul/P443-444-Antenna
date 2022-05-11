import matplotlib.pyplot as plt
import numpy as np
import os
import csv


#### Taking inputs
datasheet = 'yagi-uda5_data.txt'
shift = 'yes'
cartesian = 1
polar = 0
dB_polar = 0


#### Loading Data
def read_write(st):        # reading and writing matrix
    a=[]
    # Reading matrices from the files
    f1 = open(st, 'r')
    for line in f1.readlines():
        a.append([float(x) for x in line.split()])  # adding rows
    return a

x,y=[],[]
data = read_write(datasheet)
for i in range(len(data)):
    x.append(data[i][0])
    y.append(data[i][1])




area = 0
for i in range(len(x)-1):
    area += (y[i] + y[i+1]) * (abs(x[i] - x[i+1])) /2

isotropic_length = area / abs(x[-1] - x[0])

directivity = max(y) / isotropic_length
print(directivity)


plt.plot(x, y)
plt.title('Directivity = %s'%round(directivity,3))
plt.axhspan(0, ymax=isotropic_length, color='cyan')
plt.show()