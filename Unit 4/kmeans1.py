import pandas as pd
import numpy as np
from scipy.cluster.vq import kmeans, kmeans2, whiten
import matplotlib.pyplot as plt  


def readFile():
    dataSet = pd.read_csv("https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/un/un.csv")
    return dataSet


def main():
    dataSet = readFile()
    print(len(dataSet.index))
main()
