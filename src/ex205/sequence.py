class Sequence:

    def __init__(self,seqId='Unknown sequence',seqLetters=''):
        self.seqId=seqId
        self.letters=seqLetters

    def setSeqId(self,seqId):
        self.seqId=seqId

    def getSeqId(self):
        return self.seqId

    def setLetters(self, letters):
        self.letters=letters

    def getLetters(self):
        return self.letters


class SequenceCollection:

    def __init__(self):
        self.sequences={}

    def addSequence(self,sequence):
        seqId=sequence.getSeqId()
        self.sequences[seqId]=sequence

    def removeSequence(self,seqId):
        if seqId in self.sequences :
            del(self.sequences[seqId])

    def getSequence(self,seqId):
        res=None
        if seqId in self.sequences :
            res=self.sequences[seqId]
        return res

    def removeSequence(self,seqId):
        if seqId in self.sequences :
            del(self.sequences[seqId])

    def getAllSequences(self):
        return list(self.sequences.values())

    def len(self):
        return len(self.sequences)