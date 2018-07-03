import csv
import blast2csv
import unittest


class Blast2CsvTest(unittest.TestCase) :

    def testGenerateCsvFromBlast(self):
        self.converter=blast2csv.Blast2Csv(blastfile='../../data/blast/localblastresult.xml',csvfile='../../tmp/localblastresult.csv')
        self.converter.generateCsvFromBlast()
        allrows=[]
        with open('../../tmp/localblastresult.csv') as csvfile :
            reader=csv.DictReader(csvfile)
            for row in reader:
                allrows.append(row)
        self.assertEqual(len(allrows),20)

if __name__ == '__main__' :

    unittest.main()
