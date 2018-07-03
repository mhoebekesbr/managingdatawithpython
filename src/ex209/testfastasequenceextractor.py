import unittest

import fastadataextractor

class FastaSequenceExtractorTest(unittest.TestCase) :


    def setUp(self):
        self.extractor=fastadataextractor.FastaDataExtractor()
        self.extractor.parseFile('../../data/fasta/cyanorak_complete.faa')

    def testGetAllFastaIds(self):
        allFastaIds=self.extractor.getAllFastaIds()
        self.assertEqual(len(allFastaIds),35993)

    def testGetSequenceWithIdWholeSequence(self):
        allFastaIds=self.extractor.getAllFastaIds()
        fastaId=allFastaIds[0]
        sequence=self.extractor.getSequenceWithId(fastaId)
        self.assertEqual(len(sequence),385)

    def testGetSequenceWithIdSlice(self):
        allFastaIds=self.extractor.getAllFastaIds()
        fastaId=allFastaIds[0]
        sequence=self.extractor.getSequenceWithId(fastaId,101,151)
        self.assertEqual(len(sequence),50)

    def testGetSequenceWithIdOutsideBoundaries(self):
        allFastaIds=self.extractor.getAllFastaIds()
        fastaId=allFastaIds[0]
        with self.assertRaises(IndexError) :
            sequence=self.extractor.getSequenceWithId(fastaId,10000000,2000000)


if __name__ == '__main__' :

    unittest.main()
