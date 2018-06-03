infile = open("../../data/fasta/Syn_RCC307.faa")
lines = infile.readlines()
infile.close()
seqIds=[]
sequences=[]
for line in lines:
    line=line[:-1]
    if len(line)> 0 :
        if line[0] == '>' :
            currentSeqId=line
            seqIds.append(currentSeqId)
        else :
            currentSequence=line
            sequences.append(currentSequence)

print(seqIds[1234])
print(len(sequences[1234]))
print(sequences[1234])



