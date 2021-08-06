from pymongo import MongoClient

def getJobsFromCodeRome(codeRome):
    client = MongoClient(port=27017)
    db=client.jobMatching
    jobs=db.jobSheet.find({'metier.code':codeRome})
    listskill=[]
    n=0
    for job in jobs:
        n+=1
        for skill in job['competencesDeBase']:
            if skill['code'] not in listskill:
                if(n>1):
                    print('NOT INSIDEEEEE')
                print(skill['code'])
                print(n)
                listskill.append(skill['code'])
    return 'bjr'
listROME=['M1601', 'G1702', 'G1701', 'G1101', 'G1205', 'G1203',
 'G1202', 'E1101', 'D1501', 'A1403', 'A1402', 'A1401', 'K1303', 
 'D1505', 'D1403', 'D1401', 'H1101', 'M1606', 'N4105', 'G1605', 
 'M1401', 'N1303', 'N1105', 'G1703', 'G1502', 'G1501', 'D1503', 
 'D1502', 'N1102', 'N1103', 'H3302', 'D1214', 'D1212', 'D1211', 
 'D1210', 'D1209', 'D1107', 'D1106', 'D1506', 'G1803', 'G1801', 'M1603']

def getListRome():
    client = MongoClient(port=27017)
    db=client.jobMatching
    listjob=[]
    for job in db.jobSheet.find({}):
        if job['metier']['code'] not in listjob:
            listjob.append(job['metier']['code'])
    print(listjob)
    return 'bjr'


def createRomeFile(listRome):
    client = MongoClient(port=27017)
    db=client.jobMatching
    listjob=[]
    for jobROME in listRome:
        job = db.jobSheet.find_one({'metier.code':jobROME})
        db.romeJobSheet.insert_one(job)
    return 'bjr'

createRomeFile(listROME)