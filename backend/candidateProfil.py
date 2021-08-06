from jobSheet import JobSheet
from candidateRIASEC import CandidateRIASEC


class Candidate:
    def __init__(self, listJobScore, RIASEC,name,id):
        self.name=name,
        self.id=id
        self.jobScore=listJobScore
        self.candidateJobSheet=self.getJobSheets()
        self.dictRIASEC=RIASEC
        self.RIASEC=CandidateRIASEC(self.candidateJobSheet,RIASEC)
        self.skills=self.calculateListSkillsScore()
    
    
    def getJobSheets(self): 
        listJobSheet=[]
        for job in self.jobScore:
            listJobSheet.append({'job':JobSheet(job['jobCode']),'score':job['score']})
        return listJobSheet

    
    def calculateListSkillsScore(self):
        listSkillsScore=[]
        for job in self.candidateJobSheet:
            score=job['score']
            for skill in job['job'].competencesDeBase:
                listSkillsScore.append({'skillName':skill['skill'].libelle,'skillCode':skill['code'], 'score':score})
        return listSkillsScore

    def getSkillScore(self,skillCode):
        skills= list(filter(lambda candidateSkill: candidateSkill['skillCode'] == skillCode, self.skills))
        sumScore=0
        if (len(skills)>0):
            for skill in skills:
                sumScore+=skill['score']
            sumScore/=len(skills)
        return sumScore,len(skills)
    
    def getCandidateJobSheetInfo(self):
        listInfoJob=[]
        for job in self.candidateJobSheet:
            listInfoJob.append({
                'code':job['job'].codeOGR,
                'codeROME':job['job'].codeROME,
                'title':job['job'].libelle,
                'domaine':job['job'].domaine,
                'grandDomaine':job['job'].grandDomaine,
                'score':job['score'],
            })
        return listInfoJob
    
    def getCandidateRiasec(self):
        return  {
            'RIASEC':{
                'R':self.RIASEC.getRIASEC('R'),
                'I':self.RIASEC.getRIASEC('I'),
                'A':self.RIASEC.getRIASEC('A'),
                'S':self.RIASEC.getRIASEC('S'),
                'E':self.RIASEC.getRIASEC('E'),
                'C':self.RIASEC.getRIASEC('C'),
            },
            'JobRIASEC':{
                'R':self.RIASEC.getJobRIASEC('R'),
                'I':self.RIASEC.getJobRIASEC('I'),
                'A':self.RIASEC.getJobRIASEC('A'),
                'S':self.RIASEC.getJobRIASEC('S'),
                'E':self.RIASEC.getJobRIASEC('E'),
                'C':self.RIASEC.getJobRIASEC('C'),
            },
            'SkillsRIASEC':{
                'R':self.RIASEC.getSkillsRIASEC('R'),
                'I':self.RIASEC.getSkillsRIASEC('I'),
                'A':self.RIASEC.getSkillsRIASEC('A'),
                'S':self.RIASEC.getSkillsRIASEC('S'),
                'E':self.RIASEC.getSkillsRIASEC('E'),
                'C':self.RIASEC.getSkillsRIASEC('C'),
            },
        }
    
    def getJSONProfil(self): 

        return {
            'name':self.name,
            'id':self.id,
            'JobExperience':self.getCandidateJobSheetInfo(),
            'RIASEC':{
                'R':self.RIASEC.getRIASEC('R'),
                'I':self.RIASEC.getRIASEC('I'),
                'A':self.RIASEC.getRIASEC('A'),
                'S':self.RIASEC.getRIASEC('S'),
                'E':self.RIASEC.getRIASEC('E'),
                'C':self.RIASEC.getRIASEC('C'),
            },
            'JobRIASEC':{
                'R':self.RIASEC.getJobRIASEC('R'),
                'I':self.RIASEC.getJobRIASEC('I'),
                'A':self.RIASEC.getJobRIASEC('A'),
                'S':self.RIASEC.getJobRIASEC('S'),
                'E':self.RIASEC.getJobRIASEC('E'),
                'C':self.RIASEC.getJobRIASEC('C'),
            },
            'skills':self.skills,
        }
        



