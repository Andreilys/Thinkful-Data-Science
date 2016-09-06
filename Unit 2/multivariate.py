import pandas as pd


def loansDataClean():
    loansData = pd.read_csv("https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/loans/loansData.csv")
    loansData.dropna(inplace=True)
    return loansData


def interestRateData(loansData):
    rows = loansData['Interest.Rate'].tolist()
    df = pd.DataFrame(rows, columns={'Interest.Rate'})
    return df


def annualIncomeData(loansData):
    rows = loansData['Monthly.Income'].tolist()
    newRows = []
    for i in rows:
        i = i * 12
        newRows.append(i)
    df = pd.DataFrame(newRows, columns={'Annual.Income'})
    return df


def homeOwnershipData(loansData):
    rows = loansData['Home.Ownership'].tolist()
    df = pd.DataFrame(rows, columns={'Home.Ownership'})
    return df


def main():
    loansData = loansDataClean()
    interestRateDF = interestRateData(loansData)
    annualIncomeDF = annualIncomeData(loansData)
    homeOwnershipDF = homeOwnershipData(loansData)
    print(homeOwnershipDF['Home.Ownership'])
main()
