import sequence

seqOne=sequence.Sequence()
seqOne.setSeqId('Seq1')
seqOne.setLetters('SSDFREFREFREF')


seqTwo=sequence.Sequence()
seqTwo.setSeqId('Seq2')
seqTwo.setLetters('QDKDSKFOKOKORKFOEKSDKFDSOFKORKOFKROKFS')

seqCollection=sequence.SequenceCollection()

seqCollection.addSequence(seqOne)
seqCollection.addSequence(seqTwo)

print('Collection length is: '+str(seqCollection.len()))

seqCollection.removeSequence(seqOne.getSeqId())

print('Collection length is: '+str(seqCollection.len()))

allSequences=seqCollection.getAllSequences()

print('ID of remaining sequence is: '+allSequences[0].getSeqId())

