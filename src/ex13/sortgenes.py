import argparse

import sequencetools

parser=argparse.ArgumentParser(description='Read a set of sequences, and count the number of sequences on each strand.')
parser.add_argument('-s','--seqfile',required=True,help='A multi-fasta sequence file.')
parser.add_argument('-v','--verbose',action='store_true',help='Display a lot of information.')
args=parser.parse_args()

sequenceInfo=sequencetools.readFastaSequencesFromFile(args.seqfile)
orderedSequenceIds=sequencetools.sortSequencesByLength(sequenceInfo,sequencetools.SORTORDER_DESC)

longestSequenceId=orderedSequenceIds[0]
longestSequenceInfo=sequenceInfo[longestSequenceId]
longestSequenceLength=longestSequenceInfo[sequencetools.POSITION_MAX]-longestSequenceInfo[sequencetools.POSITION_MIN]+1

shortestSequenceId=orderedSequenceIds[-1]
shortestSequenceInfo=sequenceInfo[shortestSequenceId]
shortestSequenceLength=shortestSequenceInfo[sequencetools.POSITION_MAX]-shortestSequenceInfo[sequencetools.POSITION_MIN]+1

if args.verbose is True :
    print('Total number of sequences: '+str(len(sequenceInfo)))
print('Shortest sequence: '+str(shortestSequenceLength)+" gene: "+shortestSequenceId)
print('Longest sequence: '+str(longestSequenceLength)+" gene: "+longestSequenceId)

