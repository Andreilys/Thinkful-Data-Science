import pandas as pd
import matplotlib.pyplot as plt


def readFile():
    headers = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)", "class"]
    dataSet = pd.read_csv("https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/iris/iris.data.csv", names=headers)
    return dataSet


def scatterPlot(dataSet):
    sepalLengthDataset = dataSet[dataSet.columns[2:3]]
    sepalWidthDataset = dataSet[dataSet.columns[3:4]]
    plt.figure()
    plt.scatter(sepalLengthDataset[:50], sepalWidthDataset[:50], color="blue")
    plt.scatter(sepalLengthDataset[50:], sepalWidthDataset[50:], color="red")
    plt.show()

def knn(k):
    print(k)


def main():
    dataSet = readFile()
    scatterPlot(dataSet)
main()
