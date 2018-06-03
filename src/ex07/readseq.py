import argparse

parser=argparse.ArgumentParser(description='Read a set of sequences.')
parser.add_argument('seqfile',help='A multi-fasta sequence file.')

args=parser.parse_args()

sequenceInfo={}

SEQUENCE_KEY= 'sequence_letters'

infile = open(args.seqfile)
lines = infile.readlines()
infile.close()
for line in lines:
    line=line[:-1]
    if len(line)> 0 :
        if  line[0] == '>' :
            currentSeqId=line
        else :
            currentSequence=line
            if currentSeqId not in sequenceInfo :
                sequenceInfo[currentSeqId]={SEQUENCE_KEY : currentSequence}
            else :
                print('Duplicate sequence: '+currentSeqId)

print('Length of sequence: >CK_Syn_RCC307_1247:1103206-1103493:1|SynRCC307_1247 = '+str(len(sequenceInfo['>CK_Syn_RCC307_1247:1103206-1103493:1|SynRCC307_1247'][SEQUENCE_KEY])) )
