from osgeo import gdal
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm 
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import mpl_toolkits.mplot3d
import os
import numpy as np

#Opens the .tif file specified
def openTif(tifFilePath):
	ds = gdal.Open(tifFilePath)
	print("Finished Opening")

#Takes the information in the tif file and make it into a csv file
def convertTif(xyzFilePath):
	xyz = gdal.Translate(xyzFilePath, ds)
	xyz = None

#Creates a pandas dataframe with the new xyz file data
def loadData(xyzFilePath):
	df = pd.read_csv(xyzFilePath, sep = " ", header = None)
	df.columns = ["x","y","z"]

	print("Finished Reading")

#Plots the dataframe to a 3d model
def plotData():
    ax = plt.axes(projection="3d")
    ax.plot_trisurf(X, Y, Z)
    print("Finished Plot")
    plt.show()
    print("Plot Shown")
    
#I was running into memory issues while plotting the arrays so I made this
#To downsize the arrays by 100x to make the load lighter
def resizeArrays():
    i=0
    X = []
    x = np.array(df.x)
    
    Y = []
    y = np.array(df.y)
    
    Z = []
    z = np.array(df.z)
    
    
    for num in x:
        if(i == 100):
            X.append(num)
            i = 0
        i += 1
    print("Finished Array X")
    for num in y:
        if(i == 100):
            Y.append(num)
            i = 0
        i += 1
    print("Finished Array Y")
    for num in z:
        if(i == 100):
            Z.append(num)
            i = 0
        i += 1
    print("Finished Array Z")
        
#filepath for tif file
tifFile = 'c:/Users/James/Desktop/dataset30s/wc2.1_30s_tmin_01.tif'

#filepath for new xyz file
xyzFile = 'c:/Users/James/Desktop/dataset30s/wc2.1_30s_tmin_01.xyz'

openTif(tifFile)
#convertTif(xyzFile)
#only uncomment this code if an xyz version of the tif file isn't made yet
loadData(xyzFile)

resizeArrays()
plotData()


