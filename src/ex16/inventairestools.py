import csv

def loadInventairesCsv(filename,delimiter="\t") :
    inventairesRecords=[]
    with open(filename) as csvfile :
        reader=csv.DictReader(csvfile,delimiter=delimiter)
        for record in reader :
            inventairesRecords.append(record)
    return inventairesRecords

def buildRecordsById(records,idName='id') :
    recordsById={}
    for record in records :
        recordId=record[idName]
        recordsById[recordId]=record
    return recordsById

def loadBiotopes(filename) :
    biotopeRecords=loadInventairesCsv(filename)
    biotopesById=buildRecordsById(biotopeRecords)
    return biotopesById

def loadSpecies(filename) :
    speciesRecords=loadInventairesCsv(filename)
    speciesById=buildRecordsById(speciesRecords)
    return speciesById

def loadSpeciesNames(filename) :
    speciesNamesRecords=loadInventairesCsv(filename)
    speciesNamesById=buildRecordsById(speciesNamesRecords)
    return speciesNamesById

def loadObservations(filename) :
    observationRecords=loadInventairesCsv(filename)
    observationsById=buildRecordsById(observationRecords)
    return observationsById

