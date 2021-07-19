from requestJobInfos import getGrandDomaineDetails
class GrandDomaineSheet:

    def __init__(self, code,token=0):
        self.code=code
        grandDomaineInfos=getGrandDomaineDetails(code,token)
        self.libelle=grandDomaineInfos[0]['grandDomaine']['libelle']
        self.count=len(grandDomaineInfos)
        self.listDomaines=self.getListDomaines(grandDomaineInfos)

    def getListDomaines(self,grandDomaineInfos):
        listDomaines=[]
        for domaine in grandDomaineInfos:
            listDomaines.append(domaine['code'])
        return listDomaines