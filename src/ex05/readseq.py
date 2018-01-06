infile = open("../../data/fasta/Syn_RCC307.faa")
lines = infile.readlines()
infile.close()
sequenceInfo={}
currentSeqId=''
currentSequence=''
for line in lines:
    line=line[:-1]
    if len(line)> 0 and line[0] == '>' :
        if currentSeqId != '' :
            if currentSeqId not in sequenceInfo :
                sequenceInfo[currentSeqId]=currentSequence
                currentSequence=''
            else :
                print('Duplicate sequence: '+currentSeqId)
        currentSeqId=line
    else :
        currentSequence=currentSequence+line
if currentSeqId != '' :
    if currentSeqId not in sequenceInfo :
        sequenceInfo[currentSeqId]=currentSequence
        currentSequence=''
    else :
        print('Duplicate sequence: '+currentSeqId)

print('Length of sequence: >CK_Syn_RCC307_1247:1103206-1103493:1|SynRCC307_1247 = '+str(len(sequenceInfo['>CK_Syn_RCC307_1247:1103206-1103493:1|SynRCC307_1247'])) )
