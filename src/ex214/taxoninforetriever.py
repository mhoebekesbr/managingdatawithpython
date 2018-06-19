import json
import requests


class TaxonInfoRetriever :

    COLUMN_HEADERS = ('AphiaID', 'kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'scientificname',
                      'authority')

    BASE_URL='http://www.marinespecies.org/rest/AphiaRecordByAphiaID/'

    def __init__(self):
        pass

    def getTaxonInfoForAphiaId(self,aphiaId):
        res={}
        url=TaxonInfoRetriever.BASE_URL+str(aphiaId)
        r=requests.get(url)
        jsonString=r.text
        completeTaxonInfo=json.loads(jsonString)
        for header in TaxonInfoRetriever.COLUMN_HEADERS :
            res[header]=completeTaxonInfo[header]
        return res

