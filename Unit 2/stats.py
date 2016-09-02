import pandas as pd
from scipy import stats

def cleanData(data):
    data = [x.strip() for x in data.split('\n')]
    data = [i.split(',') for i in data]
    return data

def pandasDataFrame(data):
    column_names = data[0]
    data_rows = data[1::]
    df = pd.DataFrame(data_rows, columns=column_names)
    return df

def dfManipulator(df):
    df['Alcohol'] = df['Alcohol'].astype(float)
    df['Tobacco'] = df['Tobacco'].astype(float)

    alcoholAndTobacco = pd.concat([df['Alcohol'], df['Tobacco']])
    mean = alcoholAndTobacco.mean()
    median = alcoholAndTobacco.median()
    mode = stats.mode(alcoholAndTobacco)[0][0]
    rangeSet = max(alcoholAndTobacco) - min(alcoholAndTobacco)
    var = alcoholAndTobacco.var()
    std = alcoholAndTobacco.std()

    print("The mean, median, mode,range,variance and std for the Alcohol and Tobacco dataset is {0}, {1}, {2}, {3}, {4}, {5}"\
    .format(mean, median, mode, rangeSet, var, std))

def main():
    data = '''Region,Alcohol,Tobacco
    North,6.47,4.03
    Yorkshire,6.13,3.76
    Northeast,6.19,3.77
    East Midlands,4.89,3.34
    West Midlands,5.63,3.47
    East Anglia,4.52,2.92
    Southeast,5.89,3.20
    Southwest,4.79,2.71
    Wales,5.27,3.53
    Scotland,6.08,4.51
    Northern Ireland,4.02,4.56'''
    clean = cleanData(data)
    df = pandasDataFrame(clean)
    dfManipulator(df)

main()
