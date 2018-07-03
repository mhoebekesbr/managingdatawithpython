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

    def testGetFeaturesWithQualifier(self):
        featuresAndQualifiers=self.extractor.getFeaturesWithQualifier('locus_tag','SynRCC307_2134')
        self.assertEqual(len(featuresAndQualifiers),2)

    def testGetFeaturesWithQualifierHavingValue(self):
        featuresAndQualifiers=self.extractor.getFeaturesWithQualifier(qualifierValue='GOA:A5GVX9')
        self.assertEqual(len(featuresAndQualifiers),1)
        feature=featuresAndQualifiers[0]
        self.assertEqual(feature.type,'CDS')
        self.assertEqual(feature.start,1842317)
        self.assertEqual(feature.stop,1842866)

if __name__ == '__main__' :

    unittest.main()



