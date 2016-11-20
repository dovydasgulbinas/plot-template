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
parser.add_argument('--smooth-type', type=int, choices=range(0, 3),
                    help='0 - no smoothing, 1 - spline smoothing')
parser.add_argument('--interpolation-points', type=int, metavar='int', default=200,
                    help='lets you to set a number of interpolation points for a smooth plot')
parser.add_argument('--max-xcolumns', type=int, default=4, help='Sets the maximum number of x columns in csv file')

args = parser.parse_args(['test-data.csv', ',', '--title', 'go.nx'])
#args = parser.parse_args(['test-data.csv', ',', '--smooth-type', '1'])
#args = parser.parse_args(['--help'])
print(args)

file_name = args.data_file_name
value_separator = args.value_separator
title = args.title
name_xaxis = 'I, (A)'
name_yaxis = 'U, (V)'
display_legend = True
smooth_setting = args.smooth_type
ninterpolation_points = args.interpolation_points
yscale = 'linear'
xscale = 'linear'
xheader_char = 'x'
max_xcols = args.max_xcolumns

df = pandas.read_csv(file_name, value_separator)
ncols = len(df.columns)
headers = df.columns.values.tolist()
print("Import success!")
print(df.head())
print("Number of columns: {}".format(ncols))
print(headers)

# get all data & start ploting
x = df[df.columns[0]]
# TODO: Generate a list of cols where x is found
cols = list(df.columns)
chopped_cols = []
# Todo: aggregate valid colls to a list of lists [[x,y,yy],[xx, 2y, 2yy]]
# Generate list of columns and find the all x cols.
xheads = list(set(cols) & set([xheader_char*x for x in range(1, max_xcols)]))
xheads.sort()
xheads_len = len(xheads)

# find all x cols
for i in range(0, xheads_len):
    # get the index of x..x  occurence
    start = cols.index(xheads[i])
    # stop is the last entry between x <something> xx
    if i == xheads_len-1:
        chopped_cols.append(cols[start:])
    else:
        stop = cols.index(xheads[i+1])
        chopped_cols.append(cols[start:stop])

print(chopped_cols)


print(xheads)
# FIXME: remove exit line
exit()

xsmooth = np.array(x)
xsmooth = np.linspace(xsmooth.min(), xsmooth.max(), ninterpolation_points)
plt.xscale(xscale)
plt.yscale(yscale)

# Define axes
fig = plt.figure()
axes = fig.add_subplot(111)
axes.grid()
axes.set_xlabel(name_xaxis)
axes.set_ylabel(name_yaxis)

for i in range(1, ncols):
    y = df[df.columns[i]]

    # interpolates y values based on smooth x
    ysmooth = spline(x, y, xsmooth)
    axes.plot(xsmooth, ysmooth, label=headers[i])

if display_legend:
    plt.legend(loc='best')

# title rendering works unpredictably 
plt.title(title)
plt.show()
