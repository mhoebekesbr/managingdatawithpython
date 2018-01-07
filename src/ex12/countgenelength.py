import argparse

import sequencetools

parser=argparse.ArgumentParser(description='Read a set of sequences, and count the number of sequences on each strand.')
parser.add_argument('-s','--seqfile',required=True,help='A multi-fasta sequence file.')
parser.add_argument('-v','--verbose',action='store_true',help='Display a lot of information.')
args=parser.parse_args()

sequenceInfo=sequencetools.readFastaSequencesFromFile(args.seqfile)

minLength=None
minLengthId=None
maxLengthId=None
maxLength=None
for (sequenceId,sequenceInfo) in sequenceInfo.items() :
    seqLength=sequenceInfo[sequencetools.POSITION_MAX]-sequenceInfo[sequencetools.POSITION_MIN]+1
    if minLength is None or seqLength < minLength :
        minLength=seqLength
        minLengthId=sequenceId
    if maxLength is None or seqLength > maxLength :
        maxLength=seqLength
        maxLengthId=sequenceId

if args.verbose is True :
    print('Total number of sequences: '+str(len(sequenceInfo)))
print('Shortest sequence: '+str(minLength)+" gene: "+minLengthId)
print('Longest sequence: '+str(maxLength)+" gene: "+maxLengthId)

