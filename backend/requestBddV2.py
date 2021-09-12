from pymongo import MongoClient

def getAllROMEJobNames():
    client = MongoClient(port=27017)
    db=client.jobMatching
    ListobjectJobs=[]
    for job in db.romeJobSheet.find({}):
        ListobjectJobs.append({'code':job['metier']['code'],'name':job['metier']['libelle'],'domaine':job['metier']['domaineProfessionnel']['libelle']})
    return ListobjectJobs


def getROMEJobByCode(code):
    client = MongoClient(port=27017)
    db=client.jobMatching
    return db.romeJobSheet.find_one({'metier.code':code})

def DeleteCandidateById(id):
    client = MongoClient(port=27017)
    db=client.jobMatching
    return db.Candidate.delete_one({'id':id})

def DeleteJobByCode(code):
    client = MongoClient(port=27017)
    db=client.jobMatching
    return db.romeJobSheet.delete_one({'code':code})

# listcode=["14193","11406","N4105","10427","10659","11270","11484","10752","12764","10270","10269","10875","10386","10472","16389","10861","15095","20511","11609","13869","20546","10405"]

