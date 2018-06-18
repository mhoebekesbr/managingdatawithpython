from Bio.Blast.Applications import NcbiblastpCommandline

commandLine=NcbiblastpCommandline(query='../data/blast/candidate.fasta',db='../data/blast/cyanorak',outfmt=5,out='../data/blast/localblastresult.xml')
stdout,stderr=commandLine()

