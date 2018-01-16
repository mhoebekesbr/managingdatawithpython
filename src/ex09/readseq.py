import argparse

NUCLEOTIDES_TYPE= 'nucleotides'
RESIDUES_TYPE= 'residues'

def readFastaSequencesFromFile(filename, sequenceInfo={}, sequenceType=NUCLEOTIDES_TYPE) :
    infile = open(filename)
    lines = infile.readlines()
    infile.close()
    currentSeqId = ''
    currentSequence = ''
    for line in lines:
        line = line[:-1]
        if len(line) > 0 and line[0] == '>':
            if currentSeqId != '':
                if currentSeqId not in sequenceInfo:
                    sequenceInfo[currentSeqId] = {NUCLEOTIDES_TYPE: None, RESIDUES_TYPE: None}
                sequenceInfo[currentSeqId][sequenceType]=currentSequence
            currentSequence = ''
            currentSeqId = line
        else:
            currentSequence = currentSequence + line
    if currentSeqId != '':
        if currentSeqId not in sequenceInfo:
            sequenceInfo[currentSeqId] = {NUCLEOTIDES_TYPE: None, RESIDUES_TYPE: None}
        sequenceInfo[currentSeqId][sequenceType] = currentSequence

    return sequenceInfo



parser=argparse.ArgumentParser(description='Read a set of sequences.')
parser.add_argument('-n','--nucleotides',required=True,help='A multi-fasta sequence file with nucleotides.')
parser.add_argument('-r','--residues',required=True,help='A multi-fasta sequence file with amino acids.')
parser.add_argument('-v','--verbose',action='store_true',help='Display a lot of information.')
args=parser.parse_args()

sequenceInfo=readFastaSequencesFromFile(args.nucleotides, sequenceType=NUCLEOTIDES_TYPE)
sequenceInfo=readFastaSequencesFromFile(args.residues, sequenceInfo, sequenceType=RESIDUES_TYPE)

missingNucleotides=0
missingResidues=0

for info in sequenceInfo.values() :
    if info[NUCLEOTIDES_TYPE] is None :
        missingNucleotides=missingNucleotides+1
    if info[RESIDUES_TYPE] is None :
        missingResidues=missingResidues+1

if args.verbose is True :
    print('Total number of sequences: '+str(len(sequenceInfo)))
print('Sequences with no nucleotides: '+str(missingNucleotides))
print('Sequences with no residues: '+str(missingResidues))
