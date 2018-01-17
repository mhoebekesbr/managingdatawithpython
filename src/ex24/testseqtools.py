import logging
import sequencetools
import unittest


DATADIR='../../data'
FASTADATADIR=DATADIR+'/fasta'
GENBANKDATADIR=DATADIR+'/genbank'

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
        self.strainCollection=sequencetools.readFastaSequencesFromFile(FASTADATADIR+'/cyanorak_complete.fna',sequenceType=sequencetools.NUCLEOTIDES_TYPE)
        self.strainCollection=sequencetools.readFastaSequencesFromFile(FASTADATADIR+'/cyanorak_complete.faa',strainCollection=self.strainCollection,sequenceType=sequencetools.RESIDUES_TYPE)
        self.genbankStrain=sequencetools.readGenBankSequencesFromFile(GENBANKDATADIR+'/Syn_RCC307.gbff')

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

    def testReadSequencesFromGenbankFile(self):
        self.assertEqual(self.getbankStrain.getName(),"RCC307")
        self.assertEqual(len(self.getbankStrain.getSequences()),2535)

    def testBuildIdenticalSequenceMatches(self):
        rcc307FastaSequences=self.strainCollection.getStrainWithName('RCC307').getSequences()
        rcc307GenBankSequences=self.genbankStrain.getSequences()
        matches=sequencetools.buildIdenticalSequenceMatches(rcc307FastaSequences,rcc307GenBankSequences)
        realmatches=0
        for match in matches:
            if match[0] is not None and match[1] is not None:
                realmatches=realmatches+1
        self.assertEqual(realmatches,-1)

if __name__ == '__main__' :

    unittest.main()
