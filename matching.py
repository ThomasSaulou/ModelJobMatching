from domaineSheet import DomaineSheet
from candidateProfil import Candidate
from jobSheet import JobSheet

class Matching:

    def __init__(self, candidate, job):
        self.candidate=candidate
        self.job=job
        self.candidateJobs=self.candidate.candidateJobSheet

    def getScore(self):

        scoreFromJobScore=self.getScoreFromJobScore()
        return scoreFromJobScore
    

    def getScoreFromJobScore(self):
    
        scoreFirstDegree=self.getScoreFirstDegree()
        scoreSecondDegree=self.getScoreSecondDegree()
        return scoreFirstDegree,scoreSecondDegree


    def getScoreFirstDegree(self):

        jobScore=self.candidate.jobScore
        codeOGR=self.job.codeOGR
        for job in jobScore:
            if (job['jobCode']==codeOGR):
                return job['score']
        return 0

    def getScoreSecondDegree(self):

        jobScore=self.candidate.jobScore
        domaineCode=self.job.domaine
        score=0
        n=0
        for job in jobScore:
            jobSheet=list(filter(lambda candidateJob: candidateJob['job'].codeOGR == job['jobCode'], self.candidateJobs))[0]
            
            if(jobSheet.domaine==domaineCode):
                score+=job['score']
                n+=1
        if(n!=0):
            score/=n
        return score

    
    def getScoreFromSkills(self):
        
        jobSkills=self.job.competencesDeBase
        score=0
        n=0
        for skill in jobSkills:
            skillscore=self.candidate.getSkillScore(skill['code'])
            score+=skillscore
            if(skillscore!=0):
                n+=1
        return score/n,n,len(jobSkills)

        



listJobScore=[
    {'jobCode':'11579', 'score':70},
    {'jobCode':'13821', 'score':30},
    {'jobCode':'18088', 'score':20},
]

RIASEC={'R':20,'I':50,'A':80,'S':20,'E':70,'C':80}

print('A')
jean=Candidate(listJobScore,RIASEC)
print('B')
job=JobSheet('11578')
print(jean.getSkillScore('123248'))

print('C')
match=Matching(jean,job)
print(match.getScoreFromSkills())



