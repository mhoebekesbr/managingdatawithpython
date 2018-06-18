import unittest

import cyanosequence

class CyanoSequenceCollectiontTest(unittest.TestCase):

    def setUp(self):
        self.seqCollection=cyanosequence.CyanoSequenceCollection()
        self.seqCollection.readFastaSequencesFromFile('../../data/fasta/cyanorak_complete.faa')

    def testRaiseMissingStrainException(self):
        with self.assertRaises(cyanosequence.MissingStrainException) :
            self.seqCollection.readFastaSequencesFromFile('../../data/fasta/cyanorak_complete_bogus.faa')

    def testGetAllStrainNames(self):
        allStrainNames=self.seqCollection.getAllStrainNames()
        self.assertEqual(len(allStrainNames),14)

    def testGetSequencesInStrain(self):
        sequencesInRCC307=self.seqCollection.getSequencesInStrain('RCC307')
        self.assertEqual(len(sequencesInRCC307),2558)

if __name__ == '__main__' :

    unittest.main()