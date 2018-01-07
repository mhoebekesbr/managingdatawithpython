import argparse
import re

import sequencetools

parser=argparse.ArgumentParser(description='Read a set of sequences, and count the number of sequences on each strand.')
parser.add_argument('-s','--seqfile',required=True,help='A multi-fasta sequence file.')
parser.add_argument('-v','--verbose',action='store_true',help='Display a lot of information.')
args=parser.parse_args()

sequenceInfo=sequencetools.readFastaSequencesFromFile(args.seqfile)

leadingSequences=0
laggingsequences=0

idPattern=re.compile(r":(-?\d)\|")
for sequenceId in sequenceInfo.keys() :
    match=re.search(idPattern,sequenceId)
    if match is not None :
        strand=int(match.group(1))
        if strand >= 0 :
            leadingSequences=leadingSequences+1
        else :
            laggingsequences=laggingsequences+1
    else :
        print("Unable to extract strand information for: "+sequenceId)

if args.verbose is True :
    print('Total number of sequences: '+str(len(sequenceInfo)))
print('Sequences on leading strand: '+str(leadingSequences))
print('Sequences on lagging strand: '+str(laggingsequences))
