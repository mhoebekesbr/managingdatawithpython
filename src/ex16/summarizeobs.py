import argparse
import csv

import inventairestools

parser=argparse.ArgumentParser()
parser.add_argument("-b","--biotopes",required=True,help="Table with biotope records exported from inventaires database.")
parser.add_argument("-n","--speciesnames",required=True,help="Table with species names records exported from inventaires database.")
parser.add_argument("-o","--observations",required=True,help="Table with observation records exported from inventaires database.")
parser.add_argument("-r","--resultfile",required=True,help="Table with the observation summary results.")
parser.add_argument("-v","--verbose",action="store_true",help="Verbose mode: print lots of output.")

args=parser.parse_args()

observationsById=inventairestools.loadObservations(args.observations)
biotopesById=inventairestools.loadBiotopes(args.biotopes)
speciesNamesById=inventairestools.loadObservations(args.speciesnames)

observationSummaries=[]
for (observationId,observationRecord) in observationsById.items() :
    biotopeId=observationRecord['id_biotope']
    eunis=''
    biotope=''
    if biotopeId in biotopesById :
        biotopeRecord=biotopesById[biotopeId]
        if 'code_eunis' in biotopeRecord :
            eunis=biotopeRecord['code_eunis']
        if 'description' in biotopeRecord :
            biotope=biotopeRecord['description']
    else :
        print("Biotope identifier not found: "+str(biotopeId))

    genre=''
    espece=''
    speciesNameId=observationRecord['id_nomespece']
    if speciesNameId in speciesNamesById :
        speciesName=speciesNamesById[speciesNameId]
        if 'genre' in speciesName :
            genre=speciesName['genre']
        if 'espece' in speciesName :
            espece=speciesName['espece']
    else :
        print("Species name identifier not found: "+str(speciesNameId))

    observationSummary={ 'id' : observationId,
                        'eunis' : eunis,
                        'biotope' : biotope,
                        'genre' : genre,
                         'espece' : espece,
                         'date' : observationRecord['date']}
    observationSummaries.append(observationSummary)



with open(args.resultfile,'w') as csvfile :
    csvwriter=csv.DictWriter(csvfile,delimiter=';',fieldnames=['id','date','genre','espece','eunis','biotope'])
    csvwriter.writeheader()
    csvwriter.writerows(observationSummaries)

