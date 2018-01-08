"""SequenceTools : a Library With Handy Sequence Manipulation Functions.

SequenceTools contains a set of functions for manipulating sequence related data such as:

- functions for reading (multi-)fasta files

"""
import re

#: The constant used for specifying nucleotide sequences.
NUCLEOTIDES_TYPE= 'nucleotides'

#: The constant used for specifying amino acid sequences.
RESIDUES_TYPE= 'residues'

POSITION_MIN = 'minpos'
#: The constant used for specifying the leftmost position of a gene on a chromosome.

POSITION_MAX = 'maxpos'
#: The constant used for specifying the rightmost position of a gene on a chromosome.

STRAND = 'strand'
#: The constant used for specifying the strand of a gene on a chromosome.

SORTORDER_ASC = 'asc'
#: The constant used for specifying an ascending sort order.

SORTORDER_DESC = 'desc'
#: The constant used for specifying a descending sort order.

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
        currentSeqId = ''
        currentSequence = ''
        for line in infile:
            line = line[:-1]
            if len(line) > 0 and line[0] == '>':
                if currentSeqId != '':
                    if currentSeqId not in sequenceInfo:
                        sequenceInfo[currentSeqId] = {NUCLEOTIDES_TYPE: None, RESIDUES_TYPE: None}
                        sequenceInfo[currentSeqId] = computeSequencePositionInfo(currentSeqId,sequenceInfo[currentSeqId])
                    sequenceInfo[currentSeqId][sequenceType]=currentSequence
                    currentSequence = ''
                currentSeqId = line
            else:
                currentSequence = currentSequence + line
        if currentSeqId != '':
            if currentSeqId not in sequenceInfo:
                sequenceInfo[currentSeqId] = {NUCLEOTIDES_TYPE: None, RESIDUES_TYPE: None}
                sequenceInfo[currentSeqId] = computeSequencePositionInfo(currentSeqId, sequenceInfo[currentSeqId])
            sequenceInfo[currentSeqId][sequenceType] = currentSequence

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
    reverse=False
    if sortOrder == SORTORDER_DESC :
        reverse=True
    idsWithLengthList=[]
    for (sequenceId, sequence) in sequenceInfo.items() :
        idsWithLengthList.append({ 'id' : sequenceId, 'length' : int(sequence[POSITION_MAX]-sequence[POSITION_MIN]+1) })
    idsWithLengthList.sort(reverse=reverse,key=lambda value : value['length'])
    sortedIds=[]
    for value in idsWithLengthList :
        sortedIds.append(value['id'])
    return sortedIds

