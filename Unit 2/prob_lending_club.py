import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

def cleanData():
    loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
    loansData.dropna(inplace=True)
    rows = loansData['Amount.Requested'].tolist()
    df = pd.DataFrame(rows, columns={'Amount Requested'})
    return df


# compared to amount funded they are more or less the same, the outlier and third
# upper quartile in
# amount requested is slightly greater than that which is funded,
def boxplot(df):
    plt.figure()
    df.boxplot()
    plt.show()

# compared to amount funded, people were requesting a lot more which can be seen by
# the peak in funding from the $5000 to $10000 range and lower portions of $10k+
def histogram(df):
    plt.figure()
    df.hist()
    plt.show()

#r^2 value is slightly higher in amount funded (indicating that the line has
#a better fit for amount funded than amount requested)
def qqPlot():
    plt.figure()
    loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
    loansData.dropna(inplace=True)
    graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
    plt.show()

def main():
    df = cleanData()
    boxplot(df)
    histogram(df)
    qqPlot()

main()
