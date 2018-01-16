import logging
import sequencetools
import unittest


DATADIR='../../data/fasta'

testLogger=logging.getLogger(__name__)
testLogger.setLevel(logging.DEBUG)
consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
testLogger.addHandler(consoleHandler)

sequencetoolsLogger=logging.getLogger("sequencetools")
sequencetoolsLogger.setLevel(logging.DEBUG)
fileHandler=logging.FileHandler("testseqtools.log")
fileHandler.setLevel(logging.INFO)
fileFormatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fileHandler.setFormatter(fileFormatter)
sequencetoolsLogger.addHandler(fileHandler)

class SequenceToolsTest(unittest.TestCase):

    def setUp(self):
        self.strainCollection=sequencetools.readFastaSequencesFromFile(DATADIR+'/cyanorak_complete.fna',sequenceType=sequencetools.NUCLEOTIDES_TYPE)
        self.strainCollection=sequencetools.readFastaSequencesFromFile(DATADIR+'/cyanorak_complete.fna',strainCollection=self.strainCollection,sequenceType=sequencetools.RESIDUES_TYPE)

    def testGetStrainNames(self):
        testLogger.debug("Testing method getStrainNames()")
        strains=self.strainCollection.getStrainNames()

        self.assertEqual(len(strains),14)

    def testGetStrainByName(self):
        testLogger.debug("Testing method getStrainWithName for strain RCC307")
        rcc307=self.strainCollection.getStrainWithName('RCC307')
        self.assertEqual(len(rcc307.getSequences()),2559)

    def testGetGenesWithName(self):
        testLogger.debug("Testing method getSequencesWithGeneName for gene name pattern pet*")
        genes=self.strainCollection.getSequencesWithGeneName("pet*")
        self.assertEqual(len(genes),119)

if __name__ == '__main__' :

    unittest.main()
