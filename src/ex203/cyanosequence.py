from sequence import Sequence, SequenceCollection

class CyanoSequence(Sequence):

    def __init__(self,strain='Unknown',seqId='Unknown Cyanobacteria Sequence',letters=''):
        super().__init__(seqId,letters)
        self.strain=strain

    def setStrain(self,strain):
        self.strain=strain

    def getStrain(self):
        return self.strain

class CyanoSequenceCollection(SequenceCollection):

    def __init__(self):
        super().__init__()

    def getSequencesInStrain(self,strain):
        sequencesInStrain=[]
        for sequence in self.getAllSequences():
            if sequence.getStrain() == strain :
                sequencesInStrain.append(sequence)
        return sequencesInStrain

    def getAllStrainNames(self):
        allStrainNames=set()
        for sequence in self.getAllSequences():
            allStrainNames.add(sequence.getStrain())
        return allStrainNames

