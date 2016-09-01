from collections import defaultdict
import csv
import pandas as pd

input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')
print(input_dataframe[0:10])

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    header = next(inputFile)
    for line in inputReader:
        print(line)
        print(header)

population_dict_2010 = defaultdict(int)
population_dict_2100 = defaultdict(int)
population_dict_land = defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    header = header.rstrip().split(',')
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == "Total National Population":
            population_dict_2010[line[0]] += int(line[5])
            population_dict_2100[line[0]] += int(line[6])
            population_dict_land[line[0]] += int(line[7])


# with open('national_population.csv','w') as outputFile:
#     outputFile.write('continent,2010_population\n')
#     for k,v in population_dict.iteritems():
#         outputFile.write(k+',' +str(v) + '\n')

def populationChange(pop_dict_2010, pop_dict_2100):
    biggestGrowth = {"holder":0}
    for k in pop_dict_2010:
        changeInPopulation = pop_dict_2100[k] - pop_dict_2010[k]
        if biggestGrowth.values()[0] <= changeInPopulation:
            biggestGrowth.clear()
            biggestGrowth[k] = float(changeInPopulation)
    print(biggestGrowth.keys()[0])

populationChange(population_dict_2010, population_dict_2100)

def populationDensity(pop_dict_2010, pop_dict_land):
    densePopulation = {"holder":0}
    for k in pop_dict_2010:
        popDensity = float(pop_dict_2010[k]) / pop_dict_land[k]
        if densePopulation.values()[0] <= popDensity:
            densePopulation.clear()
            densePopulation[k] = popDensity
    print(densePopulation.keys()[0])


populationDensity(population_dict_2010, population_dict_land)
