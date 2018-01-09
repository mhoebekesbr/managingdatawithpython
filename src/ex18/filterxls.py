import argparse
import csv
import openpyxl

parser=argparse.ArgumentParser()
parser.add_argument('-i','--infile',required=True,help='XLS input data file')
parser.add_argument('-o','--outfile',required=True,help='CSV output data file')
parser.add_argument('-w','--worksheet',required=True,help='Name of worksheet containing observation data')
parser.add_argument('-c','--column',required=True,help='Name of the column containing the date information')
parser.add_argument('-y','--year',required=True,help='Cutoff Year')
args=parser.parse_args()

workbook=openpyxl.load_workbook(args.infile)
worksheet=workbook[args.worksheet]
records=[]


