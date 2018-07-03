import unittest
import taxoninforetriever

class TaxonRestrieveTest(unittest.TestCase) :


    def setUp(self):
        self.taxonretriever=taxoninforetriever.TaxonInfoRetriever()


    def testGetTaxonInfoForAphiaId(self):
        taxonInfo=self.taxonretriever.getTaxonInfoForAphiaId(130714)
        self.assertEqual(taxonInfo['kingdom'],'Animalia')
        self.assertEqual(taxonInfo['phylum'],'Annelida')
        self.assertEqual(taxonInfo['genus'],'Polygordius')

if __name__ == '__main__' :

    unittest.main()
