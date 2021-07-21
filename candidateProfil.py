from jobSheet import JobSheet
from candidateRIASEC import CandidateRIASEC


class Candidate:
    def __init__(self, listJobScore, RIASEC):
        self.jobScore=listJobScore
        self.candidateJobSheet=self.getJobSheets()
        self.RIASEC=CandidateRIASEC(self.candidateJobSheet,RIASEC)
        self.skills=self.calculateSkills()
        
    

    
    def getJobSheets(self): 
        listJobSheet=[]
        for job in self.jobScore:
            listJobSheet.append({'job':JobSheet(job['jobCode']),'score':job['score']})
        return listJobSheet

    
    def calculateSkills(self):
        listSkillsScore=[]
        for job in self.candidateJobSheet:
            score=job['score']
            for skill in job['job'].competencesDeBase:
                listSkillsScore.append({'skillCode':skill['code'], 'score':score})
        return listSkillsScore

    def getSkillScore(self,skillCode):
        skills= list(filter(lambda candidateSkill: candidateSkill['skillCode'] == skillCode, self.skills))
        sumScore=0
        if (len(skills)>0):
            for skill in skills:
                sumScore+=skill['score']
            sumScore/=len(skills)
        return sumScore
        



