infile = open("../../data/fasta/Syn_RCC307.faa")
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

print(seqIds[1234])
print(len(sequences[1234]))
print(sequences[1234])



