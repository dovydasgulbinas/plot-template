# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

data_file_path = 'test-data.csv'
value_separator = ','
title = 'ąčęėi-xxx-įšųū'
name_xaxis = 'I, (A)'
name_yaxis = 'U, (V)'
output_name = 'title-test.png'
display_legend = True
yscale = 'linear'
xscale = 'linear'


df = pandas.read_csv(data_file_path, value_separator)
ncols = len(df.columns)
headers = df.columns.values.tolist()
print("Import success!")
print(df.head())
print("Number of columns: {}".format(ncols))
print(headers)

plt.xscale(xscale)
plt.yscale(yscale)

# Define axes
fig = plt.figure()
axes = fig.add_subplot(111)
axes.grid()
axes.set_xlabel(name_xaxis)
axes.set_ylabel(name_yaxis)

# get all data & start ploting
x = df[df.columns[0]]
xsmooth = np.array(x)
xsmooth = np.linspace(xsmooth.min(), xsmooth.max(), 200)

for i in range(1, ncols):
    y = df[df.columns[i]]
    
    # interpolates y values based on smooth x
    ysmooth = spline(x, y, xsmooth)
    axes.plot(xsmooth, ysmooth, label=headers[i]) 
    
#export to .png
if display_legend:
    plt.legend(loc='best')

# title rendering works unpredictably 
plt.title(title)
plt.savefig(output_name)
