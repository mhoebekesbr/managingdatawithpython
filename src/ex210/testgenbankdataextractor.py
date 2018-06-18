import unittest
import genbankdataextractor

class TestGenbankDataExtractor(unittest.TestCase) :

    def setUp(self):
        self.extractor=genbankdataextractor.GenbankDataExtractor()
        self.extractor.parseFile('../../data/genbank/Syn_RCC307.gbk')

    def testGetFeaturesOfType(self):
        features=self.extractor.getFeaturesOfType('gene')
        self.assertEqual(len(features),2583)

    def testGetFeatureOfTypeOnStrand(self):
        features=self.extractor.getFeaturesOfType('CDS',genbankdataextractor.SimpleFeature.STRAND_LEADING)
        self.assertEqual(len(features),1287)


