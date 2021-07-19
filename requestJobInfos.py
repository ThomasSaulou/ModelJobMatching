import requests 
from accessToken import getRomeToken
import time

def getLibelleJobCodeRome():
    API_URL = 'https://api.emploi-store.fr/partenaire/rome/v1/appellation?q=N1103'
    token= getRomeToken()
    headers={'Authorization': 'Bearer '+token}
    time.sleep(0.3)
    response = requests.get(API_URL,headers= headers)
    return response.json()


def getJobDetails(code,token=0):
    API_URL = 'https://api.emploi-store.fr/partenaire/rome/v1/appellation/'+code
    if(token==0):
        token= getRomeToken()
    headers={'Authorization': 'Bearer '+token}
    time.sleep(0.3)
    response = requests.get(API_URL,headers= headers)
    return response.json() 

def getJobDetailsVTest(code,token=0):
    API_URL = 'https://api.emploi-store.fr/partenaire/rome/v1/metier/'+code
    if(token==0):
        token= getRomeToken()
    headers={'Authorization': 'Bearer '+token}
    time.sleep(0.3)
    response = requests.get(API_URL,headers= headers)
    return response.json() 


def getSkillDetails(code,token=0):
    API_URL = 'https://api.emploi-store.fr/partenaire/rome/v1/competence?code='+code
    if(token==0):
        token= getRomeToken()
    headers={'Authorization': 'Bearer '+token}
    time.sleep(0.3)
    response = requests.get(API_URL,headers= headers)
    if(response.status_code==429):
        time.sleep(float(response.headers['Retry-After']))
        response = requests.get(API_URL,headers= headers)
    return response.json() 

def getNoeudSkillDetails(code,token=0):
    API_URL = 'https://api.emploi-store.fr/partenaire/rome/v1/noeudcompetence/'+code+'/competence'
    if(token==0):
        token= getRomeToken()
    headers={'Authorization': 'Bearer '+token}
    time.sleep(0.3)
    response = requests.get(API_URL,headers= headers)
    if(response.status_code==429):
        time.sleep(float(response.headers['Retry-After']))
        response = requests.get(API_URL,headers= headers)
    return response.json() 


def getRacineSkillDetails(code,token=0):
    API_URL = 'https://api.emploi-store.fr/partenaire/rome/v1/racinecompetence/'+code+'/noeudcompetence'
    if(token==0):
        token= getRomeToken()
    headers={'Authorization': 'Bearer '+token}
    time.sleep(0.3)
    response = requests.get(API_URL,headers= headers)
    if(response.status_code==429):
        time.sleep(float(response.headers['Retry-After']))
        response = requests.get(API_URL,headers= headers)
    return response.json() 


def getDomaineDetails(code,token=0):
    API_URL = 'https://api.emploi-store.fr/partenaire/rome/v1/domaineprofessionnel/'+code+'/metier'
    if(token==0):
        token= getRomeToken()
    headers={'Authorization': 'Bearer '+token}
    time.sleep(0.3)
    response = requests.get(API_URL,headers= headers)
    if(response.status_code==429):
        time.sleep(float(response.headers['Retry-After']))
        response = requests.get(API_URL,headers= headers)
    return response.json() 

def getGrandDomaineDetails(code,token=0):
    API_URL = 'https://api.emploi-store.fr/partenaire/rome/v1/granddomaine/'+code+'/domaineprofessionnel'
    if(token==0):
        token= getRomeToken()
    headers={'Authorization': 'Bearer '+token}
    time.sleep(0.3)
    response = requests.get(API_URL,headers= headers)
    if(response.status_code==429):
        time.sleep(float(response.headers['Retry-After']))
        response = requests.get(API_URL,headers= headers)
    return response.json() 

