from requestJobInfos import getSkillDetails
from nodeSkillSheet import NodeSkillSheet
from rootSkillSheet import RootSkillSheet
from requestBdd import getSkillByCode
class SkillSheet:

    def __init__(self, codeOGR):
        self.codeOGR=codeOGR
        skillInfos=getSkillByCode(codeOGR)
        self.libelle=skillInfos['name']
        self.noeudCompetence=skillInfos['node']
        self.racineCompetence=skillInfos['root']
        self.typeCompetence=skillInfos['type']
        if(self.typeCompetence=='SavoirFaire'):
            self.riasecMineur=skillInfos['riasecMineur']
            self.riasecMajeur=skillInfos['riasecMajeur']
