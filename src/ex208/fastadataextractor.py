import Bio.SeqIO


class FastaDataExtractor() :

    def __init__(self):
        self.fastaIds=set()

    def parseFile(self,filename):
        with open(filename) as fastafile :
            for record in Bio.SeqIO.parse(fastafile,'fasta') :
                self.fastaIds.add(record.id)

    def getAllFastaIds(self):
        return self.fastaIds