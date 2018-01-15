import argparse
import json

import sequencetools

parser=argparse.ArgumentParser(description='Read a set of sequences, and count the number of sequences on each strand.')
parser.add_argument('-n','--nucseq',required=False,help='A multi-fasta nucleotide sequence file.')
parser.add_argument('-r','--residues',required=False,help='A multi-fasta amino acid sequence file.')
parser.add_argument('-o','--outfile',required=True,help='The result file in JSON format.')
parser.add_argument('-l','--list',required=False,action="store_true",help='List the strain names loaded from the fasta files.')
parser.add_argument('-s','--strain',required=False,help='A strain name.')
parser.add_argument('-g','--gene',required=False,help='A gene name pattern.')
parser.add_argument('-p','--picklefile',required=False,help='A pickle file. If the -n and -r options were also given, sequence related information will be saved in this file. Otherwise, sequence related information will be loaded from this file.')
parser.add_argument('-v','--verbose',action='store_true',help='Display a lot of information.')
args=parser.parse_args()

strainCollection=None
if args.nucseq and args.residues:
    strainCollection=sequencetools.readFastaSequencesFromFile(args.nucseq,strainCollection,sequenceType=sequencetools.NUCLEOTIDES_TYPE)
    strainCollection = sequencetools.readFastaSequencesFromFile(args.residues,strainCollection,sequenceType=sequencetools.RESIDUES_TYPE)
    if args.picklefile :
        if args.verbose :
                print("Sequence Information saved to pickle file.")
        sequencetools.saveSequenceInfoToPickleFile(args.picklefile,strainCollection)

if args.nucseq == None and args.residues == None:
    if args.picklefile :
        strainCollection=sequencetools.loadSequenceInfoFromPickleFile(args.picklefile)
        if args.verbose:
            print("Sequence Information loaded from pickle file.")

if strainCollection is None :
    print("No sequence info could be loaded. Aborting")
else :
    if args.list is not None :
        strainNames=strainCollection.getStrainNames()
        with open(args.outfile,'w') as outfile:
            json.dump(strainNames,outfile)

    if args.strain is not None :
        strain=strainCollection.getStrainWithName(args.strain)
        if strain is not None :
            dumpDictionary={'strain' : args.strain}
            sequenceList=[]
            for sequence in strain.getSequences() :
                sequenceList.append({'id': sequence.getId(),
                                     'sequence' : sequence.getSequence(),
                                     'translation' : sequence.getTranslatedSequence()})
            dumpDictionary['sequences']=sequenceList
            with open(args.outfile,'w') as outfile:
                json.dump(dumpDictionary,outfile)
        else:
            print("Strain with name "+args.strain+" not found in strain collection.")

    if args.gene is not None :
        genes=strainCollection.getSequencesWithGeneName(args.gene)
        if genes is not None :
            geneList=[]
            for sequence in genes:
                geneList.append({'id': sequence.getId(),
                                     'sequence' : sequence.getSequence(),
                                     'translation' : sequence.getTranslatedSequence()})
            with open(args.outfile,'w') as outfile:
                json.dump(geneList,outfile)

