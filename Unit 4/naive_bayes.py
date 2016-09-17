import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB


def getWeightData():
    weight_data = pd.read_csv("https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/ideal-weight/ideal_weight.csv")
    # list comprehension to get rid of the \
    weight_data.columns = [columnName.strip('\'') for columnName in weight_data.columns]
    weight_data['sex'] = [sex.strip('\'') for sex in weight_data['sex']]
    return weight_data


# finding the distribution between actual and ideal weight
def weightDistribution(weight_data_actual, weight_data_ideal):
    plt.figure()
    plt.hist(weight_data_ideal, alpha=0.8, bins=10, label="Ideal Weight")
    plt.hist(weight_data_actual, alpha=0.5, bins=10, label="Actual Weight")
    plt.legend()
    plt.show()


def differenceInWeight(weight_data_diff):
    plt.figure()
    weight_data_diff.hist()
    plt.show()


def mappingSex(sex):
    genders = []
    for i in range(len(sex)):
        if sex[i] == "Male":
            genders.append(1)
        elif sex[i] == "Female":
            genders.append(0)
    gendersDF = pd.DataFrame(genders)
    return gendersDF


# ValueError: Found arrays with inconsistent numbers of samples: [  3 182]
def naiveBayesSexClassifier(weight_data, genders):
    model = GaussianNB()
    model.fit([weight_data['ideal'], weight_data['actual'], weight_data['diff']], genders)



def main():
    weight_data = getWeightData()
    # weightDistribution(weight_data['actual'], weight_data['ideal'])
    # differenceInWeight(weight_data['diff'])
    genders = mappingSex(weight_data['sex'])
    naiveBayesSexClassifier(weight_data, genders)
main()
