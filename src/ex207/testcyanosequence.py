import logging
import unittest

import cyanosequence

cyanosequencehandler=logging.StreamHandler()
cyanosequencehandler.setLevel(logging.DEBUG)

cyanosequence.cyanoSequenceLogger.addHandler(cyanosequencehandler)
cyanosequence.cyanoSequenceLogger.setLevel(logging.DEBUG)

testhandler=logging.FileHandler('testcyanosequence.log')
testhandler.setLevel(logging.INFO)
testformatter=logging.Formatter("%(asctime)s - %(name)s - %(lineno)d - %(funcName)s - %(msg)s")
testhandler.setFormatter(testformatter)
testLogger=logging.getLogger(__name__)
testLogger.setLevel(logging.INFO)
testLogger.addHandler(testhandler)

class CyanoSequenceCollectiontTest(unittest.TestCase):

    def setUp(self):
        self.seqCollection=cyanosequence.CyanoSequenceCollection()
        self.seqCollection.readFastaSequencesFromFile('../../data/fasta/cyanorak_complete.faa')

    def testRaiseMissingStrainException(self):
        testLogger.info("Running testRaiseMissingStrainException")
        with self.assertRaises(cyanosequence.MissingStrainException) :
            self.seqCollection.readFastaSequencesFromFile('../../data/fasta/cyanorak_complete_bogus.faa')

    def testGetAllStrainNames(self):
        testLogger.info("Running testGetAllStrainNames")
        allStrainNames=self.seqCollection.getAllStrainNames()
        self.assertEqual(len(allStrainNames),14)

    def testGetSequencesInStrain(self):
        testLogger.info("Running testGetSequencesInStrain")
        sequencesInRCC307=self.seqCollection.getSequencesInStrain('RCC307')
        self.assertEqual(len(sequencesInRCC307),2558)

if __name__ == '__main__' :

    unittest.main()