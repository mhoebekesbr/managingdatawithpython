"""SequenceTools : a Library With Handy Sequence Manipulation Functions.

SequenceTools contains a set of functions for manipulating sequence related data such as:

- functions for reading (multi-)fasta files

"""
import pickle
import re
import logging

#: The constant used for specifying nucleotide sequences.
NUCLEOTIDES_TYPE= 'nucleotides'

#: The constant used for specifying amino acid sequences.
RESIDUES_TYPE= 'residues'

#: The constant used for specifying the strain key in the dictionary.
STRAIN_KEY= 'strain'

#: The constant used for specifying the sequence identifier key in the dictionary.
SEQID_KEY= 'strain'


#: The constant used for specifying the leftmost position of a gene on a chromosome.
POSITION_MIN = 'minpos'

#: The constant used for specifying the rightmost position of a gene on a chromosome.
POSITION_MAX = 'maxpos'

#: The constant used for specifying the strand of a gene on a chromosome.
STRAND = 'strand'

#: The constant used for specifying an ascending sort order.
SORTORDER_ASC = 'asc'

#: The constant used for specifying a descending sort order.
SORTORDER_DESC = 'desc'

logger=logging.getLogger("sequencetools")

class Sequence :

    def __init__(self,id=None,sequence=None):
        self.id=id
        self.sequence=sequence

    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id

    def setSequence(self,sequence):
        self.sequence=sequence

    def getSequence(self):
        return self.sequence


class CodingSequence(Sequence) :

    def __init__(self,id=None,sequence=None,translation=None):
        Sequence.__init__(self,id,sequence)
        self.translation=translation

    def setTranslatedSequence(self,translation):
        self.translation=translation

    def getTranslatedSequence(self):
        return self.translation


class Strain:

    def __init__(self,name=None):
        self.name=name
        self.sequencesById={}
        self.sequencesByGeneNames={}

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def getSequences(self):
        return self.sequencesById.values()

    def addSequence(self,sequence):
        sequenceId=sequence.getId()
        self.sequencesById[sequenceId]=sequence
        genename=re.sub(r".*\|(?P<genename>.+)$","\g<genename>",sequenceId)
        if not genename in self.sequencesByGeneNames :
            self.sequencesByGeneNames[genename]=set()
        self.sequencesByGeneNames[genename].add(sequence)

    def getSequenceWithId(self,sequenceId):
        res=None
        if sequenceId in  self.sequencesById:
            res=self.sequencesById[sequenceId]
        return res

    def delSequenceWithId(self,sequenceId):
        if sequenceId in self.sequencesById :
            del(self.sequencesById[sequenceId])

    def delSequence(self,sequence):
        sequenceId=sequence.getId()
        self.delSequenceWithId(sequenceId)

    def getSequencesWithGeneName(self,genename):
        res=[]
        for storedGenename in self.sequencesByGeneNames:
            if re.match(genename,storedGenename):
                res.extend(self.sequencesByGeneNames[storedGenename])
        return res


class StrainCollection:

    def __init__(self):
        self.strainsByName={}

    def addStrain(self,strain):
        strainName=strain.getName()
        self.strainsByName[strainName]=strain

    def delStrainWithName(self,strainName):
        if strainName in self.strainsByName:
            del(self.strainsByName[strainName])

    def delStrain(self,strain):
        strainName=strain.getName()
        self.delStrainWithName(strainName)

    def getStrainWithName(self,strainName):
        res=None
        if strainName in self.strainsByName:
            res=self.strainsByName[strainName]
        return res

    def getSequencesWithGeneName(self,genename):
        logger.info("getSequencesWithGeneName called with: "+genename)
        res=[]
        for strain in self.strainsByName.values():
            res.extend(strain.getSequencesWithGeneName(genename))
        return res

    def getStrainNames(self):
        logger.info("getStrainNames called")
        res=list(self.strainsByName.keys())
        return res



def readFastaSequencesFromFile(filename, strainCollection=None, sequenceType=NUCLEOTIDES_TYPE) :
    """Read a set of fasta sequences from a file.

    :param filename: the file containing the fasta-formatted sequences
    :param sequenceInfo: a dictionary already filled with sequences read previously (default is an empty dictionary)
    :param sequenceType: an identifier specifying the type of sequences contained in the file, either NUCLEOTIDES_TYPE (default) or RESIDUES_TYPE
    :return: a dictionary with sequence information read in the file. The keys of the dictionary are the sequence identifiers, and the entries
            of the dictionary are records. These are dictionaries with two keys : NUCLEOTIDES_TYPE for storing the nucleotide sequence, and RESIDUES_TYPE
            for storing the amino acid sequence. Depending on the sequenceType argument, one of the two entries will be filled with data read from the file.
    """

    if strainCollection is None:
        strainCollection=StrainCollection()

    with open(filename) as infile :
        currentSeqId = ''
        currentSequence = ''
        for line in infile:
            line = line[:-1]
            if len(line) > 0 and line[0] == '>':
                if currentSeqId != '':
                        strainName = re.sub(r"^CK_(?P<synpro>[^_]+)_(?P<strain>[^_]+)_.*$", r"\g<strain>", currentSeqId)
                        strain=strainCollection.getStrainWithName(strainName)
                        if strain is None:
                            strain=Strain(name=strainName)
                            strainCollection.addStrain(strain)
                        sequence=strain.getSequenceWithId(currentSeqId)
                        if sequence is None:
                            sequence=CodingSequence(id=currentSeqId)
                            strain.addSequence(sequence)
                        if sequenceType == NUCLEOTIDES_TYPE :
                            sequence.setSequence(currentSequence)
                        if sequenceType == RESIDUES_TYPE :
                            sequence.setTranslatedSequence(currentSequence)
                currentSequence = ''
                currentSeqId = line[1:]
            else:
                currentSequence = currentSequence + line
        if currentSeqId != '':
            strainName = re.sub(r"^CK_(?P<synpro>[^_]+)_(?P<strain>[^_]+)_.*$", r"\g<strain>", currentSeqId)
            strain = strainCollection.getStrainWithName(strainName)
            if strain is None:
                strain = Strain(name=strainName)
                strainCollection.addStrain(strain)
            sequence = strain.getSequenceWithId(currentSeqId)
            if sequence is None:
                sequence = CodingSequence(id=currentSeqId)
                strain.addSequence(sequence)
            if sequenceType == NUCLEOTIDES_TYPE:
                sequence.setSequence(currentSequence)
            if sequenceType == RESIDUES_TYPE:
                sequence.setTranslatedSequence(currentSequence)

    return strainCollection


def saveSequenceInfoToPickleFile(filename,strainCollection) :
    """Save sequence information to a pickle file

    :param filename: name of the file to save the pickled sequence information
    :param sequenceInfo:  the sequence information to save
    """
    with open(filename,"wb") as pfile :
        pickle.dump(strainCollection,pfile)

def loadSequenceInfoFromPickleFile(filename) :
    """Read sequence information from a previously saved pickle file

    :param filename: the filename of the pickle file
    :return: the dictionary with the sequence information
    """
    with open(filename,"rb") as pfile :
        strainCollection=pickle.load(pfile)
    return strainCollection
