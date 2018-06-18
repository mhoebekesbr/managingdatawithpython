"""SequenceTools : a Library With Handy Sequence Manipulation Functions.
SequenceTools contains a set of functions for manipulating sequence related data such as:
- functions for reading (multi-)fasta files
"""
import pickle
import re

#: The constant used for specifying nucleotide sequences.
NUCLEOTIDES_TYPE= 'nucleotides'

#: The constant used for specifying amino acid sequences.
RESIDUES_TYPE= 'residues'

#: The constant used for specifying the sequence identifier key in the dictionary.
SEQID_KEY= 'seqid'

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

def readFastaSequencesFromFile(filename, sequenceInfo={}, sequenceType=NUCLEOTIDES_TYPE) :
    """Read a set of fasta sequences from a file.
    :param filename: the file containing the fasta-formatted sequences
    :param sequenceInfo: a dictionary already filled with sequences read previously (default is an empty dictionary)
    :param sequenceType: an identifier specifying the type of sequences contained in the file, either NUCLEOTIDES_TYPE (default) or RESIDUES_TYPE
    :return: a dictionary with sequence information read in the file. The keys of the dictionary are the sequence identifiers, and the entries
            of the dictionary are records. These are dictionaries with two keys : NUCLEOTIDES_TYPE for storing the nucleotide sequence, and RESIDUES_TYPE
            for storing the amino acid sequence. Depending on the sequenceType argument, one of the two entries will be filled with data read from the file.
    """


    with open(filename) as infile :
        for line in infile:
            line = line[:-1]
            if len(line) > 0 :
                if line[0] == '>':
                    currentSeqId=line
                else:
                    currentSequence=line
                    if currentSeqId not in sequenceInfo:
                        sequenceInfo[currentSeqId] = {NUCLEOTIDES_TYPE: None, RESIDUES_TYPE: None, SEQID_KEY : currentSeqId}
                        sequenceInfo[currentSeqId] = computeSequencePositionInfo(currentSeqId,sequenceInfo[currentSeqId])
                    sequenceInfo[currentSeqId][sequenceType]=currentSequence

    return sequenceInfo

def computeSequencePositionInfo(sequenceId,sequenceRecord) :
    """Fill the position descriptors from a sequence identifier
    :param sequenceId: sequence identifier
    :param sequenceRecord: sequence record
    :return: the modified sequence record with the position descriptors filled.
    """
    sequenceRecord[POSITION_MIN]=None
    sequenceRecord[POSITION_MAX]=None
    sequenceRecord[STRAND]=None

    positionPattern=re.compile(r":(?P<posleft>\d+)-(?P<posright>\d+):(?P<strand>-?\d)\|")

    positionMatch=re.search(positionPattern,sequenceId)
    if positionMatch is not None :
        positionLeft=int(positionMatch.group('posleft'))
        positionRight=int(positionMatch.group('posright'))
        strand=int(positionMatch.group('strand'))
        if positionLeft <= positionRight :
            sequenceRecord[POSITION_MIN]=positionLeft
            sequenceRecord[POSITION_MAX]=positionRight
        else :
            sequenceRecord[POSITION_MIN]=positionRight
            sequenceRecord[POSITION_MAX]=positionLeft
        sequenceRecord[STRAND]=strand
    else :
        print("No position match found for sequence: "+sequenceId)

    return sequenceRecord

def sortSequencesByLength(sequenceInfo,sortOrder=SORTORDER_ASC) :
    """Return the sequence ids ordered by gene length
    :param sequenceInfo: a dictionary where the keys are sequence identifiers and the values are sequence information
    records containing information about the sequence position
    :param sortOrder: one of two constants SORTORDER_ASC (default) or SORTORDER_DESC defining the sort order
    :return: the list of identifiers sorted by length
    """
    idsWithLengthList=[ { 'id' : sequenceId, 'length' : int(sequence[POSITION_MAX]-sequence[POSITION_MIN]+1) } for (sequenceId, sequence) in sequenceInfo.items()]
    idsWithLengthList.sort(key=lambda value : value['length'])
    sortedIds=[ value['id'] for value in idsWithLengthList]
    return sortedIds

def saveSequenceInfoToPickleFile(filename,sequenceInfo) :
    """Save sequence information to a pickle file
    :param filename: name of the file to save the pickled sequence information
    :param sequenceInfo:  the sequence information to save
    """
    with open(filename,"wb") as pfile :
        pickle.dump(sequenceInfo,pfile)

def loadSequenceInfoFromPickleFile(filename) :
    """Read sequence information from a previously saved pickle file
    :param filename: the filename of the pickle file
    :return: the dictionary with the sequence information
    """
    with open(filename,"rb") as pfile :
        sequenceInfo=pickle.load(pfile)
    return sequenceInfo