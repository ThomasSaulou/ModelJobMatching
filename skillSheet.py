from requestJobInfos import getSkillDetails
from nodeSkillSheet import NodeSkillSheet
from rootSkillSheet import RootSkillSheet
class SkillSheet:

    def __init__(self, codeOGR):
        self.codeOGR=codeOGR
        skillInfos=getSkillDetails(codeOGR)[0]
        self.libelle=skillInfos['libelle']
        self.noeudCompetence=skillInfos['noeudCompetence']['code']
        self.racineCompetence=skillInfos['noeudCompetence']['racineCompetence']['code']
        self.typeCompetence=skillInfos['typeCompetence']
        if(self.typeCompetence=='savoir'):
            self.riasecMineur=skillInfos['riasecMineur']
            self.riasecMajeur=skillInfos['riasecMajeur']
