from pymongo import MongoClient
import random as rand

ListJobCode=['M1601', 'G1702', 'G1701', 'G1101', 'G1205', 'G1203', 'G1202', 'E1101', 'D1501', 
 'A1403', 'A1402', 'A1401', 'K1303', 'D1505', 'D1403', 'D1401', 'G1703', 'D1106', 'G1803', 'G1801']

def createListJobScore():
    randomval= rand.randrange(10)
    randomJob=[]
    for i in range(0,randomval):
        randomJob.append(rand.choice(ListJobCode))
    listJobScore=[]
    for job in randomJob:
        listJobScore.append({
        "jobCode": job,
        "score": rand.random()*100
        })
    return listJobScore

def getRand3value():
    fristnumber=rand.random()*100
    secondNumber= rand.uniform(0, 100-fristnumber)
    thirdNumber=100-fristnumber-secondNumber
    listVal=[fristnumber,secondNumber,thirdNumber]
    rand.shuffle(listVal)
    return listVal

def createNewCandidates():
    client = MongoClient(port=27017)
    db=client.jobMatching
    rand3val=getRand3value()
    
    for i in range(0,100):

        objetCandidate={
        "name": str(i+6),
        "id": str(i+6),
        "softskills": [
            {
            "name": "Être autonome",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens de l’innovation/créativité",
            "val": str(rand.random()*100)
            },
            {
            "name": "Capacité d’adaptation",
            "val": str(rand.random()*100)
            },
            {
            "name": "Curiosité intellectuelle",
            "val": str(rand.random()*100)
            },
            {
            "name": "Etre persévérant",
            "val": str(rand.random()*100)
            },
            {
            "name": "Faire preuve d’autorité",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens des responsabilités",
            "val": str(rand.random()*100)
            },
            {
            "name": "Maîtrise de soi",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens de l’organisation",
            "val": str(rand.random()*100)
            },
            {
            "name": "Orientation clients",
            "val": str(rand.random()*100)
            },
            {
            "name": "Être rigoureux",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens de la pédagogie",
            "val": str(rand.random()*100)
            },
            {
            "name": "Être à l’écoute",
            "val": str(rand.random()*100)
            },
            {
            "name": "Avoir l’esprit d’équipe",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens des relations humaines",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens des affaires et de la valeur de l’argent",
            "val": str(rand.random()*100)
            },
            {
            "name": "Faire preuve de discrétion",
            "val": str(rand.random()*100)
            },
            {
            "name": "Faire preuve de diplomatie",
            "val": str(rand.random()*100)
            },
            {
            "name": "Réactivité",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens de l’analyse",
            "val": str(rand.random()*100)
            },
            {
            "name": "Esprit de synthèse",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens critique",
            "val": str(rand.random()*100)
            },
            {
            "name": "Sens de l’initiative",
            "val": str(rand.random()*100)
            }
        ],
        "listJobScore": createListJobScore(),
        "interview": {
            "video": {
            "happy": rand3val[0],
            "sad": rand3val[1],
            "neutre": rand3val[2]
            }
        },
        "RIASEC": {
            "R": rand.random()*100,
            "I": rand.random()*100,
            "A": rand.random()*100,
            "S": rand.random()*100,
            "E": rand.random()*100,
            "C": rand.random()*100
        }
        }
        db.Candidate.insert_one(objetCandidate)


#createListJobScore()
createNewCandidates()