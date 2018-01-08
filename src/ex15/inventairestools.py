import csv

def loadBiotopes(filename) :
    biotopes=[]
    with open(filename) as csvfile :
        reader=csv.DictReader(csvfile,delimiter="\t")
        for record in reader :
            biotopes.append(record)
    return biotopes
