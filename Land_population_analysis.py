from collections import defaultdict

population_dict = defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    header = header.rstrip().split(',')
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == "Total National Population":
            population_dict[line[0]] += int(line[5])

with open('national_population.csv','w') as outputFile:
    outputFile.write('continent,2010_population\n')
    for k,v in population_dict.iteritems():
        outputFile.write(k+',' +str(v) + '\n')
