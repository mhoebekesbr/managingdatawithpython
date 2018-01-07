import argparse

import sequencetools

parser=argparse.ArgumentParser(description='Read a set of sequences.')
parser.add_argument('-n','--nucleotides',required=True,help='A multi-fasta sequence file with nucleotides.')
parser.add_argument('-r','--residues',required=True,help='A multi-fasta sequence file with amino acids.')
parser.add_argument('-v','--verbose',action='store_true',help='Display a lot of information.')
args=parser.parse_args()

sequenceInfo=sequencetools.readFastaSequencesFromFile(args.nucleotides, sequenceType=sequencetools.NUCLEOTIDES_TYPE)
sequenceInfo=sequencetools.readFastaSequencesFromFile(args.residues, sequenceInfo, sequenceType=sequencetools.RESIDUES_TYPE)

missingNucleotides=0
missingResidues=0

for info in sequenceInfo.values() :
    if info[sequencetools.NUCLEOTIDES_TYPE] is None :
        missingNucleotides=missingNucleotides+1
    if info[sequencetools.RESIDUES_TYPE] is None :
        missingResidues=missingResidues+1

if args.verbose is True :
    print('Total number of sequences: '+str(len(sequenceInfo)))
print('Sequences with no nucleotides: '+str(missingNucleotides))
print('Sequences with no residues: '+str(missingResidues))
