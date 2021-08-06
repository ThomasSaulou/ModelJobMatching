from pymongo import MongoClient

def getAllROMEJobNames():
    client = MongoClient(port=27017)
    db=client.jobMatching
    ListobjectJobs=[]
    for job in db.romeJobSheet.find({}):
        ListobjectJobs.append({'code':job['metier']['code'],'name':job['metier']['libelle']})
    return ListobjectJobs


def getROMEJobByCode(code):
    client = MongoClient(port=27017)
    db=client.jobMatching
    return db.romeJobSheet.find_one({'metier.code':code})


