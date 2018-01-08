import argparse

import sequencetools

parser=argparse.ArgumentParser(description='Read a set of sequences, and count the number of sequences on each strand.')
parser.add_argument('-s','--seqfile',required=False,help='A multi-fasta sequence file.')
parser.add_argument('-p','--picklefile',required=False,help='A pickle file. If the -s or --seqfile option was also given, sequence related information will be saved in this file. Otherwise, sequence related information will be loaded from this file.')
parser.add_argument('-v','--verbose',action='store_true',help='Display a lot of information.')
args=parser.parse_args()

sequenceInfo=None
if args.seqfile :
    sequenceInfo=sequencetools.readFastaSequencesFromFile(args.seqfile)
    if args.picklefile :
        if args.verbose :
                print("Sequence Information saved to pickle file.")
        sequencetools.saveSequenceInfoToPickleFile(args.picklefile,sequenceInfo)
else :
    if args.picklefile :
        print("Sequence Information loaded from pickle file.")
        sequenceInfo=sequencetools.loadSequenceInfoFromPickleFile(args.picklefile)

if sequenceInfo is None :
    print("No sequence info could be loaded. Aborting")
else :
    orderedSequenceIds=sequencetools.sortSequencesByLength(sequenceInfo)

    shortestSequenceId=orderedSequenceIds[0]
    shortestSequenceInfo=sequenceInfo[shortestSequenceId]
    shortestSequenceLength=shortestSequenceInfo[sequencetools.POSITION_MAX]-shortestSequenceInfo[sequencetools.POSITION_MIN]+1
    shortestSequenceStrain=sequenceInfo[shortestSequenceId][sequencetools.STRAIN_KEY]

    longestSequenceId=orderedSequenceIds[-1]
    longestSequenceInfo=sequenceInfo[longestSequenceId]
    longestSequenceLength=longestSequenceInfo[sequencetools.POSITION_MAX]-longestSequenceInfo[sequencetools.POSITION_MIN]+1
    longestSequenceStrain = sequenceInfo[longestSequenceId][sequencetools.STRAIN_KEY]

    if args.verbose is True :
        print('Total number of sequences: '+str(len(sequenceInfo)))
    print('Shortest sequence: '+str(shortestSequenceLength)+" gene: "+shortestSequenceId+", strain: "+shortestSequenceStrain)
    print('Longest sequence: '+str(longestSequenceLength)+" gene: "+longestSequenceId+", strain: "+longestSequenceStrain)

