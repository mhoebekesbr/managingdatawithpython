from Bio.Blast import NCBIWWW
import Bio.SeqIO

with open('../data/blast/candidate.fasta') as fastafile :
    records=Bio.SeqIO.parse(fastafile,'fasta')
    record=next(records)
    blastresult=NCBIWWW.qblast('blastp','nr',record.seq)
    with open('../data/blast/ncbiblastresult.xml','w') as resultfile :
        resultfile.write(blastresult.read())

