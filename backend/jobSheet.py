
from requestJobInfos import getJobDetails
from domaineSheet import DomaineSheet
from grandDomaineSheet import GrandDomaineSheet
from skillSheet import SkillSheet
from accessToken import getRomeToken
class JobSheet:

    def __init__(self, codeOGR, token=0):
        self.codeOGR = codeOGR
        jobinfos=getJobDetails(codeOGR,token)
        self.libelle=jobinfos['libelle']
        self.codeROME=jobinfos['metier']['code']
        self.libelleROME=jobinfos['metier']['libelle']
        self.RIASECMajeur=jobinfos['metier']['riasecMajeur']
        self.RIASECMineur=jobinfos['metier']['riasecMineur']
        self.codeISCO=jobinfos['metier']['codeIsco']
        self.domaine=jobinfos['metier']['domaineProfessionnel']['code']
        self.grandDomaine=jobinfos['metier']['domaineProfessionnel']['grandDomaine']['code']
        self.environnementsTravail=self.getEnvironnementsTravail(jobinfos['environnementsTravail'])
        self.competencesDeBase=self.getCompetencesDeBase(jobinfos['competencesDeBase'])

    def getEnvironnementsTravail(self,environnementsTravail):
            listEnvironnement=[]
            for environnement in environnementsTravail:
                listEnvironnement.append(environnement['code'])
            return listEnvironnement
        
    def getCompetencesDeBase(self,competencesDeBase):
            listCompetence=[]
            for competence in competencesDeBase:
                listCompetence.append({'code':competence['code'],'skill':SkillSheet(competence['code']),'competenceCle':competence['competenceCle'],'frequence':competence['frequence']})
            return listCompetence


