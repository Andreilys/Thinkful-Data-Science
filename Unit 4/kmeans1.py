import pandas as pd
import numpy as np
from scipy.cluster.vq import kmeans, kmeans2, whiten
import matplotlib.pyplot as plt


def readFile():
    dataSet = pd.read_csv("https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/un/un.csv")
    return dataSet


def plotData(dataSet):
    dataSet['lifeMale']
    dataSet['lifeFemale']
    dataSet['infantMortality']
    dataSet['GDPperCapita']
    plt.figure()
    plt.scatter(dataSet['GDPperCapita'], dataSet['lifeMale'], color="red")
    plt.show()

def main():
    dataSet = readFile()
    plotData(dataSet)
    print(dataSet['lifeMale'])
main()
