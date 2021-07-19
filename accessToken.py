import requests



def getRomeToken():
    API_URL = 'https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=%2Fpartenaire'
    CLIENT_ID='PAR_hellodoe_54c167d7d3c8addc44213a226e0400122fc8965b5708ba2cabfe5c3dafa1d3d4'
    SECRET_CODE='68bc06c328cc5f023ec38dc19cee07aa0e4f0d37832feaca056fdeb2307c7607'
    scope="api_romev1 application_PAR_hellodoe_54c167d7d3c8addc44213a226e0400122fc8965b5708ba2cabfe5c3dafa1d3d4 nomenclatureRome"
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

