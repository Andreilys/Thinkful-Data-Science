import pandas as pd
import matplotlib.pyplot as plt


def readFile():
    headers = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)", "class"]
    dataSet = pd.read_csv("https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/iris/iris.data.csv", names=headers)
    return dataSet


def scatterPlot(sepalWidthDataset, sepalLengthDataset):
    plt.figure()
    plt.scatter(sepalLengthDataset, sepalWidthDataset)
    plt.show()

def knn(k):
    print(k)


def main():
    dataSet = readFile()
    sepalLengthDataset = dataSet[dataSet.columns[0:1]]
    sepalWidthDataset = dataSet[dataSet.columns[1:2]]
    scatterPlot(sepalWidthDataset, sepalLengthDataset)
    # sepalWidthDataset = getSepalWidth(dataSet)
main()
