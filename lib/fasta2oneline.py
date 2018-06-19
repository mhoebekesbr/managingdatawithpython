#!/usr/bin/env python3

import argparse

parser=argparse.ArgumentParser(description='Convert FASTA files where sequences span multiple lines to files with single line sequences')
parser.add_argument('infile',metavar='INFILE',help='Name of FASTA input file')
parser.add_argument('outfile',metavar='OUTFILE',help='Name of FASTA input file')
args=parser.parse_args()


infile = open(args.infile)
lines = infile.readlines()
infile.close()
seqIds=[]
sequences=[]
currentSeqId=''
currentSequence=''
for line in lines:
    line=line[:-1]
    if len(line)> 0 and line[0] == '>' :
        if currentSeqId != '' :
            seqIds.append(currentSeqId)
            sequences.append(currentSequence)
        currentSeqId=line
        currentSequence=''
    else :
        currentSequence=currentSequence+line

if currentSeqId != '' :
    seqIds.append(currentSeqId)
    sequences.append(currentSequence)

with open(args.outfile,'w') as outfile :
    for index in range(0,len(seqIds)) :
        outfile.write(seqIds[index]+'\n')
        outfile.write(sequences[index]+'\n')

