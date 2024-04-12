"""
read file country data and print all lines, enter filename as command line argument

"""
from sys import argv
path=argv[1]


for line in open(path):
    id, country, continent, population, life_expectancy, gdp_per_capita = line.strip().split(",")
    print(line,end="")