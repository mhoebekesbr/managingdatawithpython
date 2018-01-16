import argparse

parser=argparse.ArgumentParser(description='Read a set of sequences.')
parser.add_argument('seqfile',help='A multi-fasta sequence file.')

args=parser.parse_args()

sequenceInfo={}

SEQUENCE_KEY= 'sequence_letters'

infile = open(args.seqfile)
lines = infile.readlines()
infile.close()
currentSeqId=''
currentSequence=''
for line in lines:
    line=line[:-1]
    if len(line)> 0 and line[0] == '>' :
        if currentSeqId != '' :
            if currentSeqId not in sequenceInfo :
                sequenceInfo[currentSeqId]={SEQUENCE_KEY : currentSequence}
            else :
                print('Duplicate sequence: '+currentSeqId)
        currentSequence = ''
        currentSeqId=line
    else :
        currentSequence=currentSequence+line
if currentSeqId != '' :
    if currentSeqId not in sequenceInfo :
        sequenceInfo[currentSeqId] = {SEQUENCE_KEY: currentSequence}
        currentSequence=''
    else :
        print('Duplicate sequence: '+currentSeqId)

print('Length of sequence: >CK_Syn_RCC307_1247:1103206-1103493:1|SynRCC307_1247 = '+str(len(sequenceInfo['>CK_Syn_RCC307_1247:1103206-1103493:1|SynRCC307_1247'][SEQUENCE_KEY])) )
