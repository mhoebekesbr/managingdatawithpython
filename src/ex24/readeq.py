import Bio.SeqIO
import BCBio.GFF
import Bio.Seq
import Bio.Alphabet

with open('../../data/genbank/Syn_RCC307.gbff') as seqfile :
    for recorddict in Bio.SeqIO.parse(seqfile,'genbank') :
        print(recorddict)
        print(recorddict.seq.alphabet)
        seqslice=recorddict.seq[10:20]
        print(seqslice)
        print(seqslice.reverse_complement())
        feature=recorddict.features[0]
        print(feature.type)
        print(feature.location)
        print(feature.qualifiers['organism'][0])


newseq=Bio.Seq.Seq('DFDFGKDGOKOKG',Bio.Alphabet.ProteinAlphabet())
print(newseq)




