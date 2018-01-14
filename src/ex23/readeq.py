import Bio.SeqIO
import BCBio.GFF

with open('../../data/fasta/Syn_RCC307.fna') as seqfile :
    recorddict=Bio.SeqIO.to_dict(Bio.SeqIO.parse(seqfile,'fasta'))
    print(recorddict)

featdict=dict(gff_id=['chr1'])
print(featdict)

