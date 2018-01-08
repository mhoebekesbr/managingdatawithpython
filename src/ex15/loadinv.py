import argparse

import inventairestools

parser=argparse.ArgumentParser()
parser.add_argument("-b","--biotopes",required=True,help="Table with biotope records exported from inventaires database.")
parser.add_argument("-v","--verbose",action="store_true",help="Verbose mode: print lots of output.")

args=parser.parse_args()

biotopes=inventairestools.loadBiotopes(args.biotopes)
print("Table contains "+str(len(biotopes))+" records.")
print("First record")
for (key,value) in biotopes[0].items() :
    if value is None :
        value=''
    print(key+"= "+value)





