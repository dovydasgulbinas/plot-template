#!/home/hermes/anaconda3/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

# Parse arguments
parser = argparse.ArgumentParser(prog='Plotter',description='Plots .csv')

parser.add_argument('data_file_name', help='File name')
parser.add_argument('value_separator', help='The character that is used to denote how values are separated')
parser.add_argument('--title', metavar='str', help='sets a figure title')

#args = parser.parse_args(['test-data.csv', ',', '--title', 'go.nx'])
args = parser.parse_args()
print(args)

file_name = args.data_file_name
value_separator = args.value_separator
title = args.title
name_xaxis = 'I, (A)'
name_yaxis = 'U, (V)'
output_name = 'title-test.png'
display_legend = True
yscale = 'linear'
xscale = 'linear'

df = pandas.read_csv(file_name, value_separator)
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
plt.show()
