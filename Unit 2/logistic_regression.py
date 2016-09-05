import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('loansData_clean.csv')

print(loansData['Interest.Rate'])

interestLessThan12 = []
for i in range(len(loansData)):
    if loansData['Interest.Rate'][i] >= 0.12:
        interestLessThan12.append(1)
    else:
        interestLessThan12.append(0)

loansData['IR_TF'] = interestLessThan12

loansData['intercept'] = [1] * len(loansData)

loansData['ind_vars'] = ["loan Amount", "FICO Score", "interest Rate", "interestLessThan12", "intercept"]

logit = sm.Logit(loansData['IR_TF'], loansData['ind_vars'])
result = logit.fit()

coeff = result.params
print(coeff)
