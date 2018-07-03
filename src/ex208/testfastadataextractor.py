import unittest

import fastadataextractor

class FastaDataExtractorTest(unittest.TestCase) :


    def setUp(self):
        self.extractor=fastadataextractor.FastaDataExtractor()
        self.extractor.parseFile('../../data/fasta/cyanorak_complete.faa')

    def testGetAllFastaIds(self):
        allFastaIds=self.extractor.getAllFastaIds()
        self.assertEqual(len(allFastaIds),35993)

if __name__ == '__main__' :

    unittest.main()
