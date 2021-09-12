from re import S
from domaineSheet import DomaineSheet
from grandDomaineSheet import GrandDomaineSheet
from candidateProfil import Candidate
from jobSheet import JobSheet
from requestBdd import getJobInfoWithCodeOGR, getAllROMEJobsWithCodeOGR
from requestBddV2 import getROMEJobByCode

class Matching:

    def __init__(self, candidate, job):
        self.candidate=candidate
        self.job=job
        self.candidateJobs=self.candidate.candidateJobSheet

    def getScore(self):

        scoreFromJobScore=self.getScoreFromJobScore()
        return scoreFromJobScore
    

    def getScoreFromJobScore(self):
    
        scoreSecondDegree=self.getScoreJOBSecondDegree()
        return scoreSecondDegree


    def getScoreSameROME(self):

        jobScore=self.candidate.jobScore
        score=0
        nbJob=0
        for job in jobScore:
            if(self.job.codeROME==job['jobCode']):
                score+=job['score']
                nbJob+=1

        return {
            'score':score,
            'nbJob':nbJob,
        }

    def getScoreJOBSecondDegree(self):

        jobScore=self.candidate.jobScore
        domaineCode=self.job.domaine
        domaine=DomaineSheet(self.job.domaine)
        nbJobInDomaine=domaine.count
        score=0
        n=0
        listDistinctJobs=[]
        for job in jobScore:
            jobSheet=getROMEJobByCode(job['jobCode'])
            if(jobSheet['metier']['domaineProfessionnel']['code']==domaineCode):
                score+=job['score']
                n+=1
                if(jobSheet['metier']['code'] not in listDistinctJobs):
                    listDistinctJobs.append(jobSheet['metier']['code'] )
        if(n!=0):
            score/=n
        return {
            'score':score,
            'count':n,
            'distinctJobs':len(listDistinctJobs),
            'nbJobInDomaine':nbJobInDomaine
        }

    def getScoreJOBThirdDegree(self):

        jobScore=self.candidate.jobScore
        grandDomaineCode=self.job.grandDomaine
        grandDomaine=GrandDomaineSheet(grandDomaineCode)
        nbJobInGrandDomaine=grandDomaine.count
        score=0
        n=0
        listDistinctJobs=[]
        for job in jobScore:
            jobSheet=getROMEJobByCode(job['jobCode'])
            if(jobSheet['metier']['domaineProfessionnel']['grandDomaine']['code']==grandDomaineCode):
                score+=job['score']
                n+=1
                if(jobSheet['metier']['domaineProfessionnel']['code'] not in listDistinctJobs):
                    listDistinctJobs.append(jobSheet['metier']['domaineProfessionnel']['code'] )
        if(n!=0):
            score/=n
        return {
            'score':score,
            'count':n,
            'distinctDomaine':len(listDistinctJobs),
            'nbJobInGrandDomaine':nbJobInGrandDomaine
        }

    
    def getScoreFromSkillsFirstDegree(self):
        
        jobSkills=self.job.competencesDeBase
        score=0
        n=0
        for skill in jobSkills:
            skillscore=self.candidate.getSkillScore(skill['code'])[0]
            score+=skillscore
            if(skillscore!=0):
                n+=1
        return {
            'score':score,
            'count':n,
            'totalSkills':len(jobSkills)
        }
    
    
    def getScoreJobKeySkills(self):
        
        jobSkills=self.job.competencesDeBase
        listKeySkills=[]
        for skill in jobSkills:
            if(skill['competenceCle']==True):

                skillscore=self.candidate.getSkillScore(skill['code'])
                infoSkill={
                    'frequence':skill['frequence'],
                    'name':skill['skill'].libelle,
                    'score':skillscore[0],
                    'count':skillscore[1]

                }
                listKeySkills.append(infoSkill)
            
        return listKeySkills

    def getScoreSoftSkills(self):
        
        candidateSoftSkills=self.candidate.softskills
        jobSoftSkills=self.job.softskills
        score=0
        amount=0
        count=0
        for skill in jobSoftSkills:
            for candidateskill in candidateSoftSkills:
                if (skill['name']==candidateskill['name']):
                    score+=float(skill['val'])*float(candidateskill['val'])
                    amount+=float(skill['val'])
        return score/amount

    def getInterviewScore(self):
        
        interview=self.candidate.interview
        videointerview=interview["video"]
        return videointerview

    def getRIASECMajeur(self):
        riasec_majeur=self.job.RIASECMajeur

        scoreRiasecMajeur=self.candidate.dictRIASEC[riasec_majeur]
        return scoreRiasecMajeur 
    
    def getRIASECMineur(self):
        riasec_mineur=self.job.RIASECMineur

        scoreRiasecMineur=self.candidate.dictRIASEC[riasec_mineur]
        return scoreRiasecMineur 
    
    def getRIASECScore(self):
        skillsRIASEC= self.candidate.getCandidateRiasec()["SkillsRIASEC"]
        jobPerCentRiasec=self.job.getPerCentRiasec()
        listRiasec=["R","I","A","S","E","C"]
        score=0
        count=0
        for riasec in listRiasec:
            count+=float(jobPerCentRiasec[riasec])
            divider=1
            if(skillsRIASEC[riasec]["count"]!=0):
                divider=skillsRIASEC[riasec]["count"]
            
            score+= int(skillsRIASEC[riasec]["score"]/divider)*float(jobPerCentRiasec[riasec])
       
        return score

    def getKeySkillAVGScore(self):
        keySkillsList= self.getScoreJobKeySkills()
        print('prout',keySkillsList)
        score=0
        for skill in keySkillsList:
            print(skill)
            score+= skill['score']
        print('scoreeee:',score)
        return score
    
   



    def getJSONMatching(self):
        return {
            'globalScore':self.getScore(),
            'softSkillScore':self.getScoreSoftSkills(),
            'scoreFromROMEJobs':self.getScoreSameROME(),
            'secondDegreeJobScore':self.getScoreJOBSecondDegree(),
            'thirdDegreeJobScore':self.getScoreJOBThirdDegree(),
            'skillScore':self.getScoreFromSkillsFirstDegree(),
            'candidateRIASEC':self.candidate.getCandidateRiasec(),
            'keySkills':self.getScoreJobKeySkills(),
            'getInterviewScore':self.getInterviewScore(),
            'RIASEC_majeur': self.getRIASECMajeur(),
            'RIASEC_mineur': self.getRIASECMineur(),
            'Skills_Riasec': self.getRIASECScore(),
            'Skill_Key_AVG_Score': self.getKeySkillAVGScore()
          
        }


        



# listJobScore=[
#     {'jobCode':'M1603', 'score':70},
#     {'jobCode':'M1603', 'score':30},
#     {'jobCode':'M1603', 'score':20},
# ]

# RIASEC={'R':20,'I':50,'A':80,'S':20,'E':70,'C':80}

# jean=Candidate(listJobScore,RIASEC,'Jean',2)
