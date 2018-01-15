import sequencetools
import unittest

DATADIR='../../data/fasta'

class SequenceToolsTest(unittest.TestCase):

    def setUp(self):
        self.strainCollection=sequencetools.readFastaSequencesFromFile(DATADIR+'/cyanorak_complete.fna',sequenceType=sequencetools.NUCLEOTIDES_TYPE)
        self.strainCollection=sequencetools.readFastaSequencesFromFile(DATADIR+'/cyanorak_complete.fna',strainCollection=self.strainCollection,sequenceType=sequencetools.RESIDUES_TYPE)

    def testGetAllString(self):
        strains=self.strainCollection.getStrainNames()
        self.assertEqual(len(strains),14)

    def testGetStrainByName(self):
        rcc307=self.strainCollection.getStrainWithName('RCC307')
        self.assertEqual(len(rcc307.getSequences()),2559)

    def testGetGenesWithName(self):
        genes=self.strainCollection.getSequencesWithGeneName("pet*")
        self.assertEqual(len(genes),119)

if __name__ == '__main__' :
    unittest.main()

