import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))


loansData['Interest.Rate'] = cleanInterestRate

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip('months')))

loansData['Loan.Length'] = cleanLoanLength


cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange.map(lambda x: [int(n) for n in x])
loansData['FICO.Range'] = cleanFICORange

ficoScore = []
for i in range(len(loansData['FICO.Range'])):
    ficoScore.append(int(loansData['FICO.Range'].values[i][0]))

loansData['FICO.Score'] = ficoScore

# plt.figure()
# p = loansData['FICO.Score'].hist()
# plt.show()

# plt.figure()
# a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
# plt.show()
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']
#
# # The dependent variable
# y = np.matrix(intrate).transpose()
# # The independent variables shaped as columns
# x1 = np.matrix(fico).transpose()
# x2 = np.matrix(loanamt).transpose()
#
# x = np.column_stack([x1,x2])
#
# X = sm.add_constant(x)
# model = sm.OLS(y,X)
# f = model.fit()
#
# print(f.summary())

loansData.to_csv('loansData_clean.csv', header=True, index=False)
