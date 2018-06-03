#!/usr/bin/env python3

# Tool to convert fasta files with multi-sequence lines to
# files with single-sequence lines.
#

import argparse
import logging
import glob
import ntpath

logging.basicConfig(level=logging.DEBUG)

def process_fastafile(filename,outputdir) :

    logging.info("Reading from file %s"%filename)
    outfile_basename=ntpath.basename(filename)
    outfilename=ntpath.join(outputdir,outfile_basename)
    logging.info("Writing to  file %s" % outfilename)

    current_seqid=None
    current_sequence=''
    with open(outfilename, "w") as outfile :
        with open(filename) as infile :
            for line in infile.readlines() :
                line=line[:-1]
                if line.startswith(">") :
                    if current_seqid is not None and current_sequence != '' :
                        outfile.write("%s\n%s\n"%(current_seqid,current_sequence))
                    current_seqid=line
                    current_sequence=''
                else :
                    current_sequence=current_sequence+line

if __name__ == '__main__' :

    parser=argparse.ArgumentParser(description='Generate single-line sequence fasta files form multi-line sequence fasta files.')
    parser.add_argument("-i","--input",help="input directory",required=True)
    parser.add_argument("-o","--output",help="output directory",required=True)
    parser.add_argument("-e","--extension",help="file extension of fasta files in input directory",required=True)

    args=parser.parse_args()

    fastafiles=glob.glob("%s/*.%s"%(args.input,args.extension))
    logging.info("Matched %d files."%len(fastafiles))

    for fastafile in fastafiles :
        process_fastafile(fastafile,args.output)




