from pymongo import MongoClient
#Step 1: Connect to MongoDB - Note: Change connection string as needed


def getJobByCode(code):
    client = MongoClient(port=27017)
    db=client.jobMatching
    return db.jobSheet.find_one({'code':code})

def getAllJobNames():
    client = MongoClient(port=27017)
    db=client.jobMatching
    ListobjectJobs=[]
    for job in db.jobSheet.find({}):
        ListobjectJobs.append({'code':job['code'],'name':job['libelle']})
    return ListobjectJobs

def getAllROMEJobNames():
    client = MongoClient(port=27017)
    db=client.jobMatching
    ListobjectJobs=[]
    for job in db.romeJobSheet.find({}):
        ListobjectJobs.append({'code':job['metier']['code'],'name':job['metier']['libelle']})
    return ListobjectJobs

def getSkillByCode(code):
    client = MongoClient(port=27017)
    db=client.jobMatching
    return db.skills.find_one({'code':code})

def getCandidateByID(id):
    client = MongoClient(port=27017)
    db=client.jobMatching
    candidate=db.Candidate.find_one({'id':id})
    return candidate

def getAllCandidatesNames():
    client = MongoClient(port=27017)
    db=client.jobMatching
    ListobjectCandidates=[]
    for candidates in db.Candidate.find({}):
        ListobjectCandidates.append({'name':candidates['name'],'id':candidates['id']})
    return ListobjectCandidates

def createNewCandidate(listJobScore,RIASEC,name,id):
    client = MongoClient(port=27017)
    db=client.jobMatching
    
    objetCandidate={
            'name':name,
            'id':id,
            'listJobScore':listJobScore,
            'RIASEC':RIASEC,
        }
    db.Candidate.insert_one(objetCandidate)


def getJobInfoWithCodeOGR(codeOGR):
    client = MongoClient(port=27017)
    db=client.jobMatching
    job=db.jobSheet.find_one({'code':codeOGR})
    return job

def getAllROMEJobsWithCodeOGR(codeOGR):
    client = MongoClient(port=27017)
    db=client.jobMatching
    job=db.jobSheet.find_one({'code':codeOGR})
    codeROme=job['metier']['code']
    allJobs=db.jobSheet.find({'metier.code':codeROme})
    return allJobs


