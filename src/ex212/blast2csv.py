import Bio.Blast.NCBIXML
import csv

class Blast2Csv :

    DEFAULT_FIELDNAMES=['queryname','subjectname','qstart','qend']

    def __init__(self,blastfile=None,csvfile=None):
        self.blastfile=blastfile
        self.csvfile=csvfile


    def setBlastFile(self,blastfile):
        self.blastfile=blastfile

    def setCsvFile(self,csvfile):
        self.csvfile=csvfile


    def generateCsvFromBlast(self):
        with open(self.blastfile) as blastfile :
            with open(self.csvfile,'w',newline='') as csvfile :
                writer=csv.DictWriter(csvfile,fieldnames=Blast2Csv.DEFAULT_FIELDNAMES,delimiter='\t')
                writer.writeheader()
                for record in Bio.Blast.NCBIXML.parse(blastfile) :
                    row={}
                    row['queryname']=record.query
                    for alignment in record.alignments :
                        row['subjectname']=alignment.title
                        for hsp in alignment.hsps :
                            row['qstart']=hsp.query_start
                            row['qend']=hsp.query_end
                            writer.writerow(row)



