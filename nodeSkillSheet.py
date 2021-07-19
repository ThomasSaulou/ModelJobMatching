


#getNoeudSkillDetails('00169')
from requestJobInfos import getNoeudSkillDetails
class NodeSkillSheet:

    def __init__(self, codeOGR):
        self.codeOGR=codeOGR
        nodeInfo=getNoeudSkillDetails(codeOGR)
        self.skills=self.getSkillsList(nodeInfo)
        self.libelle=nodeInfo[0]['noeudCompetence']['libelle']
        self.count=len(nodeInfo)

    def getSkillsList(self, nodeInfo):
        listSkills=[]
        for skill in nodeInfo:
            listSkills.append(skill['code'])
        return listSkills