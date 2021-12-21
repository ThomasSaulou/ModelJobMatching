import requests



def getRomeToken():
    API_URL = 'https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=%2Fpartenaire'
    data ={
        'grant_type':'client_credentials',
        'client_id':CLIENT_ID,
        'client_secret':SECRET_CODE,
        'scope': scope,
    }
    headers={
    'Content-Type':	'application/x-www-form-urlencoded'
    }
    response = requests.post(API_URL,headers=headers,data= data)
    return response.json()['access_token']

