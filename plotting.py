import matplotlib.pyplot as plt
import numpy as np
import os
import csv


#### Taking inputs
datasheet = 'yagi-uda5_data.txt'
shift = 'no'
cartesian = 0
polar = 1
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


#### Shifting Axis
if shift == 'yes':
    max, max_sl = 0, 0
    for i in range(len(y)):
        if y[i]>max:
            max = y[i]
            max_sl = i
    new_zero = x[max_sl]
    for i in range(len(x)):
        x[i] = x[i]-new_zero


#### Cartesian Graph
if cartesian==1:
    plt.plot(x,y,label='Polar graph')
    plt.grid()
    plt.fill_between(x, 0, y, color='cyan')
    plt.show()


#### Polar Graph
if polar==1:
    r = y
    theta = np.deg2rad(x)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)
    ax.set_rmax(2)
    ax.set_rticks([20, 40, 60, 80, 100])  # Less radial ticks
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    ax.set_title("Field Pattern of yagi-uda 5 element antenna in Polar Axis", va='bottom')
    plt.show()


#### Polar Graph in dB
if dB_polar==1:
    y_dB = [20 * np.log10(y[i]) for i in range(len(y))]
    r = y_dB
    theta = np.deg2rad(x)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)
    ax.set_rmax(2)
    ax.set_rticks([0, 10, 20, 30, 40, 50])
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    ax.set_title("Field Pattern of folded dipole antenna in Polar Axis", va='bottom')
    plt.show()


