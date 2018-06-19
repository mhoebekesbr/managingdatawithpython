import json
import requests

class InterproInfoRetriever :

    DEFAULT_FIELDS=('name','description','GO')

    BASE_URL='https://www.ebi.ac.uk/ebisearch/ws/rest/interpro/entry/'

    def getInterproInfoForEntry(self,interproId,fields=DEFAULT_FIELDS):
        res=[]
        url=InterproInfoRetriever.BASE_URL+interproId+'?fields='+','.join(fields)
        r=requests.get(url,headers={'Accept':'application/json'})
        interproCompleteResponse=json.loads(r.text)
        interproEntries=interproCompleteResponse['entries']
        for entry in interproEntries :
            entryFields=entry['fields']
            resEntry={}
            for field in fields :
                if field in entryFields :
                    resEntry[field]=entryFields[field]
            res.append(resEntry)
        return res




