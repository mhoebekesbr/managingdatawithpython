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
