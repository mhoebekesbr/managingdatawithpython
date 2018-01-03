#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Synopsis : readseqwithargs.py is a trivial program read sequences in a multi-fasta file.
Author : Mark HOEBEKE (mark.hoebeke@sb-roscoff.fr)

"""
import argparse

parser=argparse.ArgumentParser(description='Read a set of sequences.')
parser.add_argument('-n','--nucleotides',required=True,help='A multi-fasta sequence file with nucleotides.')
parser.add_argument('-r','--residues',required=True,help='A multi-fasta sequence file with amino acids.')
parser.add_argument('-v','--verbose',action='store_true',help='Display a lot of information.')
args=parser.parse_args()

sequenceInfo={}

NUCLEOTIDES_KEY='nucleotides'
RESIDUES_KEY='residues'

infile = open(args.nucleotides)
lines = infile.readlines()
infile.close()
currentSeqId=''
currentSequence=''
for line in lines:
    line=line[:-1]
    if len(line)> 0 and line[0] == '>' :
        if currentSeqId != '' :
            if currentSeqId not in sequenceInfo :
                sequenceInfo[currentSeqId]={NUCLEOTIDES_KEY : currentSequence, RESIDUES_KEY : None}
                currentSequence=''
            else :
                print('Duplicate sequence: '+currentSeqId)
        currentSeqId=line
    else :
        currentSequence=currentSequence+line
if currentSeqId != '' :
    if currentSeqId not in sequenceInfo :
        sequenceInfo[currentSeqId] = {NUCLEOTIDES_KEY: currentSequence, RESIDUES_KEY: None}
        currentSequence=''
    else :
        print('Duplicate sequence: '+currentSeqId)

infile = open(args.residues)
lines = infile.readlines()
infile.close()
currentSeqId=''
currentSequence=''
for line in lines:
    line=line[:-1]
    if len(line)> 0 and line[0] == '>' :
        if currentSeqId != '' :
            if currentSeqId not in sequenceInfo :
                sequenceInfo[currentSeqId]={RESIDUES_KEY : currentSequence, NUCLEOTIDES_KEY : None}
            else :
                sequenceInfo[currentSeqId][RESIDUES_KEY]=currentSequence
        currentSequence = ''
        currentSeqId=line
    else :
        currentSequence=currentSequence+line
if currentSeqId != '' :
    if currentSeqId not in sequenceInfo :
        sequenceInfo[currentSeqId] = {RESIDUES_KEY: currentSequence, NUCLEOTIDES_KEY: None}
    else :
        sequenceInfo[currentSeqId][RESIDUES_KEY] = currentSequence

missingNucleotides=0
missingResidues=0

for info in sequenceInfo.values() :
    if info[NUCLEOTIDES_KEY] is None :
        missingNucleotides=missingNucleotides+1
    if info[RESIDUES_KEY] is None :
        missingResidues=missingResidues+1

if args.verbose is True :
    print('Total number of sequences: '+str(len(sequenceInfo)))
print('Sequences with no nucleotides: '+str(missingNucleotides))
print('Sequences with no residues: '+str(missingResidues))
