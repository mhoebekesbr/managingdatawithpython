import cyanosequence

seqOne=cyanosequence.CyanoSequence()
seqOne.setStrain('Strain A')
seqOne.setSeqId('Seq1')
seqOne.setLetters('SSDFREFREFREF')


seqTwo=cyanosequence.CyanoSequence()
seqTwo.setStrain('Strain A')
seqTwo.setSeqId('Seq2')
seqTwo.setLetters('QDKDSKFOKOKORKFOEKSDKFDSOFKORKOFKROKFS')

seqThree=cyanosequence.CyanoSequence()
seqThree.setStrain('Strain B')
seqThree.setSeqId('Seq3')
seqThree.setLetters('SDFRFJOJFMSDCQSDSDKOKOKFORKF')

seqCollection=cyanosequence.CyanoSequenceCollection()

seqCollection.addSequence(seqOne)
seqCollection.addSequence(seqTwo)
seqCollection.addSequence(seqThree)

strains=seqCollection.getAllStrainNames()
print('Strains in the collection: ')
for strain in strains :
    print(strain)

strainASequences=seqCollection.getSequencesInStrain('Strain A')
print('Sequences in Strain A')
for sequence in strainASequences :
    print(sequence.getSeqId())
