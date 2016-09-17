import pandas as pd
import numpy as np
from sklearn.cross_validation import KFold


def getLoansData():
    loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
    loansData.dropna(inplace=True)
    rows = loansData['Amount.Requested'].tolist()
    df = pd.DataFrame(rows, columns={'Amount Requested'})
    return df

def main():
    loans_data = getLoansData()
    print(loans_data)
    kf = KFold(10, n_folds=2)
    for train, test in kf:
        print("%s %s" % (train,test))
main()
