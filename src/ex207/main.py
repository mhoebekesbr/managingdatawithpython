import logging
import cyanosequence


seqCollection=cyanosequence.CyanoSequenceCollection()
seqCollection.readFastaSequencesFromFile('../../data/fasta/cyanorak_complete_bogus.faa')

numberOfSequences=seqCollection.len()
print('Sequence collection contains: '+str(numberOfSequences)+' sequences')

sequencesPerStrain=[]
allStrains=seqCollection.getAllStrainNames()
for strain in allStrains :
    sequencesInStrain=seqCollection.getSequencesInStrain(strain)
    sequencesPerStrain.append((strain,len(sequencesInStrain)))

sequencesPerStrain.sort(reverse=True, key=lambda e : e[1])

for seqStrainInfo in sequencesPerStrain :
    print('Strain: '+seqStrainInfo[0]+' has '+str(seqStrainInfo[1])+' sequences')

