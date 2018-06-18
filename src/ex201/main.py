import sequence

seqOne=sequence.Sequence()
seqOne.setSeqId('Seq1')
seqOne.setLetters('SSDFREFREFREF')
print('SeqOne: ' + seqOne.getSeqId() +', ' + seqOne.getLetters())


seqTwo=sequence.Sequence()
seqTwo.setSeqId('Seq2')
seqTwo.setLetters('QDKDSKFOKOKORKFOEKSDKFDSOFKORKOFKROKFS')

print('SeqTwo: ' + seqTwo.getSeqId() +', ' + seqTwo.getLetters())
