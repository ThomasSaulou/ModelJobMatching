
from requestJobInfos import getJobDetails
from domaineSheet import DomaineSheet
from grandDomaineSheet import GrandDomaineSheet
from skillSheet import SkillSheet
from accessToken import getRomeToken
from requestBddV2 import getROMEJobByCode
class JobSheet:

    def __init__(self, codeOGR, token=0):
        self.codeOGR = codeOGR
        jobinfos=getROMEJobByCode(str(codeOGR))
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
        self.softskills=jobinfos['softskills']

    def getEnvironnementsTravail(self,environnementsTravail):
            listEnvironnement=[]
            for environnement in environnementsTravail:
                listEnvironnement.append(environnement['code'])
            return listEnvironnement
        
    def getCompetencesDeBase(self,competencesDeBase):
            listCompetence=[]
            for competence in competencesDeBase:
                skillsheet=SkillSheet(competence['code'])
                listCompetence.append({'code':competence['code'],'skill':skillsheet,'competenceCle':competence['competenceCle'],'frequence':competence['frequence']})
            return listCompetence



    def getPerCentRiasec(self):
            riasec={
                "R":0,
                "I":0,
                "A":0,
                "S":0,
                "E":0,
                "C":0,
            }
            total=0
            for competence in self.competencesDeBase:
                skillsheet=SkillSheet(competence['code'])
                if (skillsheet.typeCompetence=='SavoirFaire'):
                    riasec[skillsheet.riasecMajeur]+=1
                    total+=1
            riasec["R"]/=total
            riasec["I"]/=total
            riasec["A"]/=total
            riasec["S"]/=total
            riasec["E"]/=total
            riasec["C"]/=total
            print('riri',riasec)


            return riasec
