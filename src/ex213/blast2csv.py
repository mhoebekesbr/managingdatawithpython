import csv
import Bio.Blast.NCBIXML

class Blast2Csv :

    DEFAULT_FIELDNAMES=['queryname','subjectname','qstart','qend','alignlength','alignpercent']

    def __init__(self,blastfile=None,csvfile=None):
        self.blastfile=blastfile
        self.csvfile=csvfile
        self.minalignpercent=None
        self.identitypercent=None

    def setBlastFile(self,blastfile):
        self.blastfile=blastfile

    def setCsvFile(self,csvfile):
        self.csvfile=csvfile

    def setMinAlignPercent(self,perc):
        self.minalignpercent=perc

    def generateCsvFromBlast(self):

        with open(self.blastfile) as blastfile :
            with open(self.csvfile,'w',newline='') as csvfile :
                writer=csv.DictWriter(csvfile,fieldnames=Blast2Csv.DEFAULT_FIELDNAMES,delimiter='\t')
                writer.writeheader()
                for record in Bio.Blast.NCBIXML.parse(blastfile) :
                    row={}
                    row['queryname']=record.query
                    qlength=record.query_letters
                    for alignment in record.alignments :
                        alength=alignment.length
                        row['alignlength']=alength
                        row['alignpercent']=float(alength)/float(qlength)
                        if  self.minalignpercent is None or row['alignpercent'] >= self.minalignpercent :
                            row['subjectname']=alignment.title
                            for hsp in alignment.hsps :
                                row['qstart']=hsp.query_start
                                row['qend']=hsp.query_end
                                writer.writerow(row)



