import Bio.SeqIO

class SimpleFeature :

    STRAND_LEADING='ld'
    STRAND_LAGGING='lg'

    def __init__(self,type=None,start=None,stop=None,strand=None):
        self.type=type
        self.start=start
        self.stop=stop
        self.strand=strand
        self.qualifiers={}

    def setType(self,type):
        self.type=type

    def getType(self):
        return self.type

    def setStart(self,start):
        self.start=start

    def getStart(self):
        return self.start

    def setStop(self,stop):
        self.stop=stop

    def getStop(self):
        return self.stop

    def setStrand(self,strand):
        self.strand=strand

    def getStrand(self):
        return self.strand

    def setQualifiers(self,qualifiers):
        self.qualifiers=qualifiers

    def getQualifiers(self):
        return self.qualifiers


class GenbankDataExtractor() :

    def __init__(self):
        self.featureInfo=set()
        pass

    def parseFile(self,filename):
        with open (filename) as genbankfile :
            for record in Bio.SeqIO.parse(genbankfile,'gb') :
                for feature in record.features :
                    newSimpleFeature=SimpleFeature()
                    newSimpleFeature.setType(feature.type)
                    newSimpleFeature.setStart(feature.location.start)
                    newSimpleFeature.setStop(feature.location.end)
                    if feature.location.strand >= 0 :
                        newSimpleFeature.setStrand(SimpleFeature.STRAND_LEADING)
                    else :
                        newSimpleFeature.setStrand(SimpleFeature.STRAND_LAGGING)
                    newSimpleFeature.setQualifiers(feature.qualifiers)
                    self.featureInfo.add(newSimpleFeature)

    def getFeaturesOfType(self,featureType,strand=None):
        res=[]
        for feature in self.featureInfo :
            if feature.type == featureType :
                if strand == None or feature.strand == strand :
                    res.append(feature)
        res.sort(key=lambda f : f.getStart())
        return res

    def getFeaturesWithQualifier(self,qualifierName=None,qualifierValue=None) :
        res=[]
        for feature in self.featureInfo :
            candidateQualifiers=[]
            if qualifierName is None :
                candidateQualifiers.extend(feature.qualifiers.keys())
            else :
                for (qName,qValues) in feature.qualifiers.items() :
                    if qualifierValue in qValues :
                        candidateQualifiers.append(qName)
            for qualifier in candidateQualifiers :
                if qualifierValue is None or qualifierValue in feature.qualifiers[qualifier] :
                    res.append(feature)
                    break

        return res



