


#getNoeudSkillDetails('00169')
from requestJobInfos import getRacineSkillDetails
class RootSkillSheet:

    def __init__(self, codeOGR):
        self.codeOGR=codeOGR
        rootInfo=getRacineSkillDetails(codeOGR)
        self.libelle=rootInfo[0]['racineCompetence']['libelle']
        self.count=len(rootInfo)
        self.nodeSkills=self.getNodeSkillsList(rootInfo)

    def getNodeSkillsList(self, rootInfo):
        listSkills=[]
        for skill in rootInfo:
            listSkills.append(skill['code'])
        return listSkills