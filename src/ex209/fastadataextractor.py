import Bio.SeqIO

import logging

class FastaDataExtractor() :

    def __init__(self):
        self.fastaSequences={}

    def parseFile(self,filename):
        with open(filename) as fastafile :
            for record in Bio.SeqIO.parse(fastafile,'fasta') :
                self.fastaSequences[record.id]=record.seq

    def getAllFastaIds(self):
        allIdsSorted=list(self.fastaSequences.keys())
        allIdsSorted.sort()
        return allIdsSorted


    def getSequenceWithId(self,seqId,minpos=0,maxpos=-1):
        res=None
        if seqId in self.fastaSequences :
            seqRecord=self.fastaSequences[seqId]
            sequence=seqRecord
            if minpos > len(sequence) or maxpos > len(sequence) :
                raise IndexError
            res=sequence[minpos:maxpos]
        return res
