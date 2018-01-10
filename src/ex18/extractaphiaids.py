import argparse
import csv
import openpyxl

parser=argparse.ArgumentParser()
parser.add_argument('-i','--infile',required=True,help='XLS input data file')
parser.add_argument('-o','--outfile',required=True,help='CSV output data file')
parser.add_argument('-w','--worksheet',required=True,help='Name of worksheet containing observation data')
parser.add_argument('-a','--aphiaid',required=True,help='Name of the column containing the AphiaId')
parser.add_argument('-g','--genus',required=True,help='Name of the column containing the genus')
parser.add_argument('-s','--species',required=True,help='Name of the column containing the species')
args=parser.parse_args()

workbook=openpyxl.load_workbook(args.infile)
worksheet=workbook[args.worksheet]
aphiaidColumn=args.aphiaid
genusColumn=args.genus
speciesColumn=args.species

row=2
records=[]
aphiaIds=set()
while row <= worksheet.max_row :
    aphiaIdCell=worksheet[aphiaidColumn+str(row)]
    if aphiaIdCell is not None :
        aphiaId=aphiaIdCell.value
        if aphiaId is not None and not aphiaId in aphiaIds:
            aphiaIds.add(aphiaId)
            genus=worksheet[genusColumn+str(row)].value
            species=worksheet[speciesColumn+str(row)].value
            record={'aphiaid' : aphiaId, 'genus' : genus, 'species' : species}
            records.append(record)
    row=row+1

records.sort(key=lambda d : d['aphiaid'])
with open(args.outfile,'w') as csvfile :
    writer=csv.DictWriter(csvfile,delimiter=",",fieldnames=['genus','species','aphiaid'])
    writer.writeheader()
    writer.writerows(records)





