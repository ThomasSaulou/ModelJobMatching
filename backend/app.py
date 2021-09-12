from jobSheet import JobSheet
from flask import Flask, json, render_template
from requestBdd import getJobByCode, getAllJobNames, getCandidateByID, getAllCandidatesNames, createNewCandidate
from requestBddV2 import getAllROMEJobNames,getROMEJobByCode
from flask import jsonify, request
from flask_cors import CORS
from bson import ObjectId
from candidateProfil import Candidate
from matching import Matching


app = Flask(__name__)
CORS(app)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



@app.route("/job/<code>", methods =['GET'])
def getJob(code):
    job=getROMEJobByCode(code)
    return JSONEncoder().encode(job)

@app.route("/jobs", methods =['GET'])
def getAllJobs():
    return jsonify({'list':getAllROMEJobNames()})


@app.route("/candidate/<id>", methods =['GET'])
def candidateByID(id):
    candidate=getCandidateByID(str(id))
    objectCandidate=Candidate(candidate['listJobScore'],candidate['RIASEC'],candidate['name'],candidate['id'],candidate['softskills'],candidate['interview']  )
    return jsonify({'result':objectCandidate.getJSONProfil()})



@app.route("/candidates", methods =['GET'])
def getAllCandidates():
    return jsonify({'list':getAllCandidatesNames()})


@app.route("/matching", methods=['GET', 'POST'])
def getMatchingResult():
    content = request.json
    candidate=getCandidateByID(str(content['candidateId']))
    objectCandidate=Candidate(candidate['listJobScore'],candidate['RIASEC'],candidate['name'],candidate['id'],candidate['softskills'],candidate['interview'] )
    job=JobSheet(content['missionCode'])  
    matching=Matching(objectCandidate,job)
    return jsonify({'result':matching.getJSONMatching()})

@app.route("/createcandidate", methods=['GET', 'POST'])
def getMatchingResult2():
    content = request.json
    createNewCandidate(content['listJobScore'],content['RIASEC'],content['name'],content['ID'])
    return 'OK'

