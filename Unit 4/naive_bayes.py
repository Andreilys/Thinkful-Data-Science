import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
import numpy as np

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


def naiveBayesSexClassifier(weight_data, genders):
    # change to a 1D array for Gaussian function
    Y = np.ravel(genders)
    weight_ideal = weight_data['ideal'].reshape(182,1)
    weight_actual = weight_data['actual'].reshape(182,1)
    weight_diff = weight_data['diff'].reshape(182,1)
    weight_list = []
    for i in range(len(weight_data)):
        weight_list.append([int(weight_actual[i]), int(weight_ideal[i]), int(weight_diff[i])])
    X = np.array(weight_list)
    model = GaussianNB()
    model.fit(X, Y)
    # convert prediction from 1 to
    first_prediction = convertPrediction(model.predict([[145, 165, -15]]))
    second_prediction = convertPrediction(model.predict([[160, 145, 15]]))

    # first prediction:
    print("The sex for an actual weight of 145, an ideal weight of 160, and a \
    diff of -15 is {0}".format(first_prediction))
    print("Predict the sex for an actual weight of 160, an ideal weight of 145, \
    and a diff of 15 is {0}.".format(second_prediction))

def convertPrediction(prediction):
    if prediction == 1:
        prediction = "Male"
    else:
        prediction = "Female"
    return prediction

def main():
    weight_data = getWeightData()
    # weightDistribution(weight_data['actual'], weight_data['ideal'])
    # differenceInWeight(weight_data['diff'])
    genders = mappingSex(weight_data['sex'])
    naiveBayesSexClassifier(weight_data, genders)
main()
