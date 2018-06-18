import logging
import re
import sequencetools
from sequence import Sequence, SequenceCollection

cyanoSequenceLogger=logging.getLogger(__name__)

class MissingStrainException(Exception) :

    def __init__(self,wrongId):
        self.wrongId=wrongId

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
        cyanoSequenceLogger.debug("Returning sequences for strain: "+strain)
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


    def readFastaSequencesFromFile(self,filename):
        allSequences=sequencetools.readFastaSequencesFromFile(filename,sequenceType=sequencetools.RESIDUES_TYPE)
        for (seqId,seqDict) in allSequences.items() :
            cyanoSequence=CyanoSequence()
            cyanoSequence.setSeqId(seqId)
            strain = re.sub(r"^>CK_(?P<synpro>[^_]+)_(?P<strain>[^_]+)_.*$", r"\g<strain>", seqId)
            if (strain == seqId) :
                cyanoSequenceLogger.warning('Sequence :' + seqId + ' does not contain a strain identifier')
                raise MissingStrainException(seqId)
            cyanoSequence.setStrain(strain)
            cyanoSequence.setLetters(seqDict[sequencetools.RESIDUES_TYPE])
            self.addSequence(cyanoSequence)