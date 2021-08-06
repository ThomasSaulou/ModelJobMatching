
from requestJobInfos import getDomaineDetails

class DomaineSheet:

    def __init__(self, code,token=0):
        self.code=code
        domaineInfos=getDomaineDetails(code,token)
        self.libelle=domaineInfos[0]['domaineProfessionnel']['libelle']
        self.grandDomaine=domaineInfos[0]['domaineProfessionnel']['grandDomaine']['code']
        self.count=len(domaineInfos)
        self.listJob=self.getListJob(domaineInfos)

    
    def getListJob(self,domaineInfos):
        listJob=[]
        for job in domaineInfos:
            listJob.append(job['code'])
        return listJob
        



# domaine=DomaineSheet('11579')