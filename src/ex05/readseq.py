infile = open("../../data/fasta/Syn_RCC307.faa")
lines = infile.readlines()
infile.close()
sequenceInfo={}
for line in lines:
    line=line[:-1]
    if len(line)> 0 :
        if line[0] == '>' :
            currentSeqId=line
        else :
            currentSequence=line
            if currentSeqId not in sequenceInfo :
                sequenceInfo[currentSeqId]=currentSequence
            else :
                print('Duplicate sequence: '+currentSeqId)

print('Length of sequence: >CK_Syn_RCC307_1247:1103206-1103493:1|SynRCC307_1247 = '+str(len(sequenceInfo['>CK_Syn_RCC307_1247:1103206-1103493:1|SynRCC307_1247'])) )
