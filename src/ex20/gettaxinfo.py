import argparse
import csv
import configparser
import json
import requests


BASEURL='http://www.marinespecies.org/rest/AphiaRecordByAphiaID/'

parser=argparse.ArgumentParser()
parser.add_argument('-i','--infile',help='CSV file where the last column of each line contains an AphiaID')
parser.add_argument('-o','--outfile',help='CSV file with the taxonomic information extracted from WoRMS')
parser.add_argument('-c','--configfile',help='configuration file with input and ouput file format parameters.')
parser.add_argument('-w','--writeconfig',help='write the default configuration for input and ouput file format parameters.')

args=parser.parse_args()

ALL_COLUMN_HEADERS=['AphiaID','kingdom','phylum','class','order','family','genus','scientificname','authority']

config=configparser.ConfigParser()
if args.configfile is not None:
    config.read(args.configfile)
else:
    config['outfile']={}
    for header in ALL_COLUMN_HEADERS:
        config['outfile'][header]='yes'

allTaxonInfo=[]
column_headers=[]
for header in ALL_COLUMN_HEADERS:
    if config['outfile'].getboolean(header) is True :
        column_headers.append(header)

with open(args.infile) as csvfile :
    reader=csv.DictReader(csvfile)
    for record in reader :
        aphiaid=record['aphiaid']
        url=BASEURL+aphiaid
        r=requests.get(url)
        jsonString=r.text
        completeTaxonInfo=json.loads(jsonString)
        summaryTaxonInfo={}
        for header in column_headers :
            summaryTaxonInfo[header]=completeTaxonInfo[header]
        allTaxonInfo.append(summaryTaxonInfo)

with open(args.outfile,'w') as csvfile :
    writer=csv.DictWriter(csvfile,fieldnames=column_headers,delimiter=";")
    writer.writeheader()
    writer.writerows(allTaxonInfo)

if args.writeconfig is not None:
    with open(args.writeconfig,'w') as cfgfile:
        config.write(cfgfile)








