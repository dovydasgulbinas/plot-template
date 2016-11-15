# -*- coding: utf-8 -*-
import pandas
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

data_file_path = 'test.csv'
name_xaxis = 'I, (A)'
name_yaxis = 'U, (V)'
output_name = 'test-test.png'

df = pandas.read_csv(data_file_path, sep='\t')
ncols = len(df.columns)
print("Import success!")
print(df.head())
print("Number of columns: {}".format(ncols))

fig = plt.figure()

# Define axes
axes = fig.add_subplot(111)
axes.grid()
axes.set_xlabel(name_xaxis)
axes.set_ylabel(name_yaxis)

# get all data & start ploting
x = df[df.columns[0]]
for i in range(1, ncols):
    y = df[df.columns[i]]
    axes.plot(x,y) 
    
#export to .png
plt.savefig(output_name)
