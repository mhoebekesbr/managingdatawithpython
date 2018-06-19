import unittest
import interproinforetriever

class InterproInfoRetriever(unittest.TestCase) :

    def setUp(self):
        self.interproInfoRetriever=interproinforetriever.InterproInfoRetriever()


    def testGetInterproInfoForEntry(self):
        res=self.interproInfoRetriever.getInterproInfoForEntry('IPR000850')
        self.assertEqual(len(res),1)
        entry=res[0]
        self.assertEqual(len(entry['GO']),3)

