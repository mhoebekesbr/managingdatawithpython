import argparse
import csv
import json
import requests


BASEURL='http://www.marinespecies.org/rest/AphiaRecordByAphiaID/'

parser=argparse.ArgumentParser()
parser.add_argument('-i','--infile',help='CSV file where the last column of each line contains an AphiaID',required=True)
parser.add_argument('-o','--outfile',help='CSV file with the taxonomic information extracted from WoRMS',required=True)
args=parser.parse_args()

COLUMN_HEADERS=['AphiaID','kingdom','phylum','class','order','family','genus','scientificname','authority']

allTaxonInfo=[]
with open(args.infile) as csvfile :
    reader=csv.DictReader(csvfile)
    for record in reader :
        aphiaid=record['aphiaid']
        url=BASEURL+aphiaid
        r=requests.get(url)
        jsonString=r.text
        completeTaxonInfo=json.loads(jsonString)
        summaryTaxonInfo={}
        for header in COLUMN_HEADERS :
            summaryTaxonInfo[header]=completeTaxonInfo[header]
        allTaxonInfo.append(summaryTaxonInfo)

with open(args.outfile,'w') as csvfile :
    writer=csv.DictWriter(csvfile,fieldnames=COLUMN_HEADERS,delimiter=";")
    writer.writeheader()
    writer.writerows(allTaxonInfo)









