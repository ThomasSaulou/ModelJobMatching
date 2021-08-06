


class CandidateRIASEC:
    def __init__(self, candidateJobSheet,RIASEC=0):
        self.RIASEC=RIASEC
        self.candidateJobSheet=candidateJobSheet

    def getRIASEC(self,riasecLetter):
            score=self.RIASEC[riasecLetter]
            return score
        
    def getJobRIASEC(self,riasecLetter):
            jobSheetList=self.candidateJobSheet
            objectRiasec={'R':{'score':0,'count':0},'I':{'score':0,'count':0},'A':{'score':0,'count':0},'S':{'score':0,'count':0},'E':{'score':0,'count':0},'C':{'score':0,'count':0}}
            for job in jobSheetList:
                print('YOYOYOYO')
                objectRiasec[job['job'].RIASECMajeur]['score']+=job['score']
                objectRiasec[job['job'].RIASECMajeur]['count']+=1
            
            return objectRiasec[riasecLetter]

    def getSkillsRIASEC(self,riasecLetter):
            jobSheetList=self.candidateJobSheet
            objectRiasec={'R':{'score':0,'count':0},'I':{'score':0,'count':0},'A':{'score':0,'count':0},'S':{'score':0,'count':0},'E':{'score':0,'count':0},'C':{'score':0,'count':0}}
            for job in jobSheetList:
                for skills in job['job'].competencesDeBase:
                    if skills['skill'].typeCompetence=='SavoirFaire':
                        objectRiasec[skills['skill'].riasecMajeur]['score']+=job['score']
                        objectRiasec[skills['skill'].riasecMajeur]['count']+=1
            
            return objectRiasec[riasecLetter]

        
    
        

